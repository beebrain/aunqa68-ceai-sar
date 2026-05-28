import os
import re

def link_content(text):
    # Regex to match evidence codes (including Thai characters like สมอ)
    pattern = re.compile(r'\b(AUNQA-[a-zA-Z0-9\-\u0e00-\u0e7f]+)\b')
    
    lines = text.split('\n')
    new_lines = []
    
    for line in lines:
        # If the line is a comment or a section title or a table format line, skip
        trimmed = line.strip()
        if trimmed.startswith('%') or trimmed.startswith('\\section') or trimmed.startswith('\\subsection') or trimmed.startswith('\\subsubsection'):
            new_lines.append(line)
            continue
            
        # We will use re.sub with a replacement function
        def replace_match(match):
            full_match = match.group(1)
            start_pos = match.start()
            
            # Check context before the match on this line
            prefix = line[:start_pos]
            
            # 1. Skip if it is inside a LaTeX comment on the same line (if % is before it)
            # Find if there is an unescaped % before start_pos
            # Simple check: search for % and see if it's not preceded by \
            percent_match = re.search(r'(?<!\\)%', prefix)
            if percent_match:
                return full_match
                
            # 2. Skip if preceded by commands or labels like \evidence{ or ref: or app: or ref{
            # Let's check trailing characters of prefix
            if prefix.endswith('\\evidence{') or prefix.endswith('ref:') or prefix.endswith('app:') or prefix.endswith('ref{') or prefix.endswith('ref:AUNQA-') or prefix.endswith('app:AUNQA-'):
                return full_match
                
            # 3. Skip if preceded by \hyperlink{ref: or \hypertarget{ref: or similar
            if '\\hyperlink' in prefix or '\\hypertarget' in prefix:
                # Let's count braces to see if it's inside
                # If we are inside the arguments, skip it.
                # A simple heuristic: if prefix has more opening braces '{' than closing braces '}' for hyperlink
                open_braces = prefix.count('{')
                close_braces = prefix.count('}')
                if open_braces > close_braces:
                    return full_match
            
            # If all checks pass, wrap it in a hyperlink to the Master List entry
            return f"\\hyperlink{{ref:{full_match}}}{{{full_match}}}"
            
        new_line = pattern.sub(replace_match, line)
        new_lines.append(new_line)
        
    return '\n'.join(new_lines)

def main():
    sections_dir = "/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/sections"
    
    for filename in os.listdir(sections_dir):
        if filename.endswith(".tex"):
            # Skip the appendix itself since it defines the targets
            if filename == "13_appendix.tex" or filename == "01_toc.tex":
                continue
                
            filepath = os.path.join(sections_dir, filename)
            with open(filepath, "r") as f:
                content = f.read()
                
            new_content = link_content(content)
            
            if new_content != content:
                with open(filepath, "w") as f:
                    f.write(new_content)
                print(f"Updated links in {filename}")
            else:
                print(f"No raw links to update in {filename}")

if __name__ == "__main__":
    main()
