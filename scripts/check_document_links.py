"""Verify local links in the portfolio; no network calls or extra dependencies."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = sorted([ROOT / "README.md", ROOT / "SETUP.md", *ROOT.glob("portfolio/**/*.md")])
MARKDOWN = re.compile(r"!?\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
errors = []
checked = 0

for document in DOCUMENTS:
    content = document.read_text(encoding="utf-8")
    links = [match.group(1) for match in MARKDOWN.finditer(content)]
    links.extend(match.group(1) for match in HTML.finditer(content))
    for link in links:
        if not link or link.startswith("#"):
            continue
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or link.startswith("//"):
            if parsed.scheme.lower() in {"javascript", "vbscript"}:
                errors.append(f"{document.relative_to(ROOT)}: unsafe URL scheme")
            continue
        target = (document.parent / unquote(parsed.path)).resolve()
        checked += 1
        if not target.is_relative_to(ROOT):
            errors.append(f"{document.relative_to(ROOT)}: local link escapes project")
        elif not target.exists():
            errors.append(f"{document.relative_to(ROOT)}: missing local target {parsed.path}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print(f"Validated {checked} local links in {len(DOCUMENTS)} documentation files.")
