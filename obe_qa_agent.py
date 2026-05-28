#!/usr/bin/env python3
"""
OBE / AUN-QA Agent — CLI สำหรับตอบคำถามประกันคุณภาพหลักสูตร CPE&AI มรอ. 2568
ใช้ MiniMax API (OpenAI-compatible) อ่าน key จาก ~/.continue/config.yaml
"""

import os
import sys
import json
import readline
import yaml
from pathlib import Path
from datetime import datetime

import openai
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).parent
WIKI = BASE / "aun-qa-wiki"
SKILLS = BASE / "skills"
HISTORY_FILE = BASE / ".agent_history.json"
CONTINUE_CONFIG = Path.home() / ".continue" / "config.yaml"

console = Console()


def load_minimax_config() -> tuple[str, str, str]:
    """อ่าน apiKey, apiBase, model จาก ~/.continue/config.yaml"""
    if CONTINUE_CONFIG.exists():
        cfg = yaml.safe_load(CONTINUE_CONFIG.read_text(encoding="utf-8"))
        defaults = cfg.get("minimax_defaults", {})
        api_key  = defaults.get("apiKey", "")
        api_base = defaults.get("apiBase", "https://api.minimax.io/v1")
        # หา model แรกที่มี role chat
        for m in cfg.get("models", []):
            if "chat" in m.get("roles", []):
                model = m.get("model", "MiniMax-M2.7")
                break
        else:
            model = "MiniMax-M2.7"
        if api_key:
            return api_key, api_base, model

    # fallback: env var
    api_key = os.environ.get("MINIMAX_API_KEY", "")
    return api_key, "https://api.minimax.io/v1", "MiniMax-M2.7"


_api_key, _api_base, _model = load_minimax_config()
client = openai.OpenAI(api_key=_api_key, base_url=_api_base)

# ─── Knowledge base loader ────────────────────────────────────────────────────

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def load_system_prompt() -> str:
    """Build static system prompt from skills."""
    obe_concepts  = _read(SKILLS / "aunqa_criteria_knowledge" / "SKILL.md")
    aun_criteria  = _read(SKILLS / "aunqa_criteria_knowledge" / "CRITERIA.md")
    obe_writer    = _read(SKILLS / "obe_response_writer"      / "SKILL.md")
    qa_auditor    = _read(SKILLS / "qa_review_auditor"        / "SKILL.md")
    evidence_map  = _read(SKILLS / "evidence_mapper"          / "SKILL.md")

    return f"""คุณคือ **OBE/AUN-QA Expert Agent** สำหรับหลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CPE&AI) มหาวิทยาลัยราชภัฏอุตรดิตถ์ พ.ศ. 2568

## บทบาทของคุณ
คุณมีความเชี่ยวชาญ 3 โหมด ที่สลับกันได้ตามคำสั่งผู้ใช้:
1. **ผู้ช่วยตอบคำถาม** — ตอบคำถาม OBE/AUN-QA อย่างละเอียด พร้อมอ้างอิงหลักฐาน
2. **ผู้ร่างคำตอบ SAR** — ร่างคำตอบตาม 5-ส่วน (ระบบ/กลไก → การดำเนินการ → หลักฐาน → ผลลัพธ์ → การปรับปรุง)
3. **ผู้ตรวจ (Auditor)** — ตรวจคำตอบและให้ Readiness Level: Low/Medium/High

## หลักการตอบ
- ตอบเป็นภาษาไทย กระชับ ชัดเจน ใช้ภาษาประกันคุณภาพ
- อ้างอิงหลักฐาน AUNQA-X-Y หรือ AUNQA-C-S-N เมื่อมีข้อมูล
- ห้ามแต่งข้อมูล — หากไม่มีข้อมูลให้ระบุชัดว่า "ยังไม่มีข้อมูล / ต้องการหลักฐานเพิ่ม"
- ทุกคำตอบต้องเชื่อมโยง PLO/CLO และ Constructive Alignment

---

## ความรู้ OBE

{obe_concepts}

---

## เกณฑ์ AUN-QA (8 Criteria)

{aun_criteria}

---

## แนวทางร่างคำตอบ SAR

{obe_writer}

---

## แนวทางตรวจคำตอบ (Auditor)

{qa_auditor}

---

## การจับคู่หลักฐาน

{evidence_map}
"""


def load_knowledge_base() -> str:
    """Load wiki knowledge base (will be cached by API)."""
    files = [
        WIKI / "concepts" / "plo-program-learning-outcomes.md",
        WIKI / "concepts" / "clo-course-learning-outcomes.md",
        WIKI / "concepts" / "aun-qa.md",
        WIKI / "concepts" / "yleo.md",
        WIKI / "summaries" / "clo-ylo-mapping.md",
        WIKI / "summaries" / "teaching-activities.md",
        WIKI / "summaries" / "evidence-index.md",
        WIKI / "summaries" / "support-data-summary.md",
        WIKI / "summaries" / "clo-all-courses-detailed.md",
    ]
    parts = []
    for f in files:
        content = _read(f)
        if content:
            parts.append(f"### {f.name}\n\n{content}")

    return "\n\n---\n\n".join(parts) if parts else "(ไม่พบข้อมูล wiki)"


# ─── Commands ─────────────────────────────────────────────────────────────────

COMMANDS = {
    "/help":     "แสดงคำสั่งทั้งหมด",
    "/criteria": "/criteria [1-8] — เน้นตอบเกณฑ์ที่ระบุ",
    "/write":    "สลับเป็นโหมดร่างคำตอบ SAR",
    "/review":   "สลับเป็นโหมด Auditor ตรวจคำตอบ",
    "/ask":      "สลับกลับโหมดถาม-ตอบปกติ",
    "/evidence": "แสดงรายการ evidence codes ที่มี",
    "/save":     "บันทึกประวัติการสนทนา",
    "/clear":    "ล้างประวัติการสนทนา (เริ่มใหม่)",
    "/exit":     "ออกจากโปรแกรม",
}

MODE_PROMPTS = {
    "ask":    "",
    "write":  "\n\n**[โหมดร่างคำตอบ SAR]** ร่างคำตอบตาม 5 ส่วน: ระบบ/กลไก → การดำเนินการ → หลักฐาน → ผลลัพธ์ → การปรับปรุง",
    "review": "\n\n**[โหมด Auditor]** ตรวจคำตอบและให้ Review Report + Readiness Level",
}


def handle_command(cmd: str, history: list, mode: list) -> bool:
    """Process slash commands. Returns True if handled."""
    parts = cmd.strip().split(maxsplit=1)
    base  = parts[0].lower()
    arg   = parts[1] if len(parts) > 1 else ""

    if base == "/help":
        for c, desc in COMMANDS.items():
            console.print(f"  [cyan]{c}[/cyan] — {desc}")
        return True

    if base == "/criteria" and arg:
        criteria_map = {
            "1": "Criterion 1: Expected Learning Outcomes",
            "2": "Criterion 2: Programme Structure and Content",
            "3": "Criterion 3: Teaching and Learning Approach",
            "4": "Criterion 4: Student Assessment",
            "5": "Criterion 5: Academic Staff Quality",
            "6": "Criterion 6: Student Support and Advice",
            "7": "Criterion 7: Facilities and Infrastructure",
            "8": "Criterion 8: Programme Outcome Enhancement",
        }
        name = criteria_map.get(arg, f"Criterion {arg}")
        history.append({"role": "user", "content": f"ฉันต้องการให้เน้นตอบเกี่ยวกับ {name} เป็นหลัก"})
        console.print(f"[green]โฟกัสที่ {name}[/green]")
        return True

    if base == "/write":
        mode[0] = "write"
        console.print("[yellow]สลับเป็นโหมดร่างคำตอบ SAR[/yellow]")
        return True

    if base == "/review":
        mode[0] = "review"
        console.print("[yellow]สลับเป็นโหมด Auditor[/yellow]")
        return True

    if base == "/ask":
        mode[0] = "ask"
        console.print("[yellow]สลับกลับโหมดถาม-ตอบปกติ[/yellow]")
        return True

    if base == "/evidence":
        console.print("[cyan]Evidence codes ใน wiki:[/cyan]")
        ev_text = _read(WIKI / "summaries" / "evidence-index.md")
        # show just the SAR master registry table
        lines = ev_text.split("\n")
        in_table = False
        for line in lines:
            if "AUNQA-1-1" in line:
                in_table = True
            if in_table:
                console.print(line)
            if in_table and line.strip() == "" and "AUNQA" not in line:
                break
        return True

    if base == "/save":
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out = BASE / f"conversation_{ts}.json"
        out.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        console.print(f"[green]บันทึกแล้ว: {out.name}[/green]")
        return True

    if base == "/clear":
        history.clear()
        console.print("[yellow]ล้างประวัติการสนทนาแล้ว[/yellow]")
        return True

    if base == "/exit":
        console.print("[dim]ออกจากโปรแกรม[/dim]")
        sys.exit(0)

    return False


# ─── Main chat ────────────────────────────────────────────────────────────────

def chat(user_input: str, history: list, system_prompt: str, kb_content: str, mode: list) -> str:
    """Send message to MiniMax via OpenAI-compatible API."""
    mode_suffix = MODE_PROMPTS.get(mode[0], "")

    messages = [
        {"role": "system",    "content": system_prompt},
        {"role": "user",      "content": "ข้อมูล knowledge base ของหลักสูตร CPE&AI มรอ. 2568 มีดังนี้:\n\n" + kb_content},
        {"role": "assistant", "content": "รับทราบ ฉันได้โหลด knowledge base ของหลักสูตร CPE&AI มรอ. 2568 เรียบร้อยแล้ว พร้อมตอบคำถามครับ"},
        *history,
        {"role": "user",      "content": user_input + mode_suffix},
    ]

    response = client.chat.completions.create(
        model=_model,
        max_tokens=4096,
        temperature=0.2,
        messages=messages,
    )

    answer = response.choices[0].message.content
    history.append({"role": "user",      "content": user_input})
    history.append({"role": "assistant", "content": answer})

    usage = response.usage
    if usage:
        console.print(f"[dim]Tokens: input {usage.prompt_tokens:,} | output {usage.completion_tokens:,}[/dim]")

    return answer


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    if not _api_key:
        console.print("[red]ไม่พบ MiniMax API key[/red]")
        console.print(f"  ตรวจสอบ: {CONTINUE_CONFIG}")
        console.print("  หรือตั้งค่า: export MINIMAX_API_KEY='sk-cp-...'")
        sys.exit(1)

    console.print(Panel(
        "[bold cyan]OBE / AUN-QA Expert Agent[/bold cyan]\n"
        f"หลักสูตร วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ มรอ. 2568\n"
        f"Model: [yellow]{_model}[/yellow]  |  พิมพ์ [cyan]/help[/cyan] เพื่อดูคำสั่ง | [cyan]/exit[/cyan] เพื่อออก",
        title="AunQA68 Agent — MiniMax",
        border_style="cyan",
    ))

    console.print("[dim]กำลังโหลด knowledge base...[/dim]")
    system_prompt = load_system_prompt()
    kb_content    = load_knowledge_base()
    console.print(f"[dim]โหลดแล้ว: {len(kb_content):,} ตัวอักษร[/dim]\n")

    history: list = []
    mode: list    = ["ask"]  # mutable so handle_command can modify

    # readline history
    if HISTORY_FILE.exists():
        try:
            readline.read_history_file(str(HISTORY_FILE))
        except Exception:
            pass

    while True:
        mode_label = {"ask": "", "write": "[ร่าง] ", "review": "[ตรวจ] "}.get(mode[0], "")
        try:
            user_input = input(f"\n{mode_label}คุณ: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]ออกจากโปรแกรม[/dim]")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            handle_command(user_input, history, mode)
            continue

        with console.status("[cyan]กำลังคิด...[/cyan]"):
            answer = chat(user_input, history, system_prompt, kb_content, mode)

        console.print("\n[bold green]Agent:[/bold green]")
        console.print(Markdown(answer))

    # save readline history
    try:
        readline.write_history_file(str(HISTORY_FILE))
    except Exception:
        pass


if __name__ == "__main__":
    main()
