(function () {
  const input = document.querySelector("[data-search-input]");
  const toggle = document.querySelector("[data-nav-toggle]");
  const sidebar = document.querySelector("[data-sidebar]");

  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
  }

  if (!input) return;

  const depth = (location.pathname.match(/\//g) || []).length;
  const base = depth > 1 ? "../".repeat(depth - 1) : "./";
  const indexUrl = base + "search-index.json";

  let index = null;
  let panel = null;

  function ensurePanel() {
    if (panel) return panel;
    panel = document.createElement("div");
    panel.className = "search-results";
    panel.setAttribute("role", "listbox");
    document.body.appendChild(panel);
    return panel;
  }

  function positionPanel() {
    const rect = input.getBoundingClientRect();
    panel.style.left = rect.left + "px";
    panel.style.top = rect.bottom + 6 + "px";
    panel.style.width = Math.max(rect.width, 320) + "px";
  }

  function highlight(text, q) {
    if (!q) return text;
    const re = new RegExp("(" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
    return text.replace(re, "<mark>$1</mark>");
  }

  function search(q) {
    if (!index || q.length < 2) {
      panel.classList.remove("visible");
      return;
    }
    const ql = q.toLowerCase();
    const hits = index
      .filter((item) => {
        const blob = (item.title + " " + item.text).toLowerCase();
        return blob.includes(ql);
      })
      .slice(0, 12);

    if (!hits.length) {
      panel.innerHTML = '<div style="padding:0.75rem;color:#5c6b7a">ไม่พบผลลัพธ์</div>';
      panel.classList.add("visible");
      positionPanel();
      return;
    }

    panel.innerHTML = hits
      .map((item) => {
        const url = base + item.url;
        const snippet = (item.text || "").slice(0, 120);
        return (
          '<a href="' +
          url +
          '" role="option">' +
          '<div class="sr-title">' +
          highlight(item.title, q) +
          "</div>" +
          (snippet ? '<div class="sr-snippet">' + highlight(snippet, q) + "…</div>" : "") +
          "</a>"
        );
      })
      .join("");
    panel.classList.add("visible");
    positionPanel();
  }

  fetch(indexUrl)
    .then((r) => r.json())
    .then((data) => {
      index = data;
    })
    .catch(() => {});

  input.addEventListener("input", () => {
    ensurePanel();
    search(input.value.trim());
  });

  input.addEventListener("focus", () => {
    if (input.value.trim().length >= 2) {
      ensurePanel();
      search(input.value.trim());
    }
  });

  document.addEventListener("click", (e) => {
    if (panel && !panel.contains(e.target) && e.target !== input) {
      panel.classList.remove("visible");
    }
  });

  window.addEventListener("resize", () => {
    if (panel && panel.classList.contains("visible")) positionPanel();
  });
})();
