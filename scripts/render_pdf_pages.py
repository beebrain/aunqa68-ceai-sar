import argparse
import os

import fitz  # PyMuPDF


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, help="Path to PDF")
    ap.add_argument("--out", required=True, help="Output directory")
    ap.add_argument("--start", type=int, default=1, help="1-based start page")
    ap.add_argument("--end", type=int, default=1, help="1-based end page (inclusive)")
    ap.add_argument("--dpi", type=int, default=160)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    doc = fitz.open(args.pdf)
    start0 = max(0, args.start - 1)
    end0 = min(doc.page_count - 1, args.end - 1)
    for i in range(start0, end0 + 1):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=args.dpi)
        out_path = os.path.join(args.out, f"p{i+1:03}.png")
        pix.save(out_path)

    print(f"Rendered pages {args.start}-{args.end} to {args.out}")


if __name__ == "__main__":
    main()

