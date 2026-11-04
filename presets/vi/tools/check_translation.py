#!/usr/bin/env python3
"""Check that the Vietnamese translation keeps every machine-relevant token of
the English originals.

Pairs checked:
  * templates/X.md            <-> presets/vi/templates/X.md
  * templates/commands/X.md   <-> presets/vi/commands/speckit.X.md
  * docs/X.md                 <-> docs/vi/X.md   (every docs/vi page except GLOSSARY.md)

For every pair it compares:
  * YAML frontmatter (all keys and values, except human-readable text fields)
  * placeholders: __SPECKIT_*__, $ARGUMENTS-style, {SCRIPT}-style, [ALL_CAPS]
  * [NEEDS CLARIFICATION] markers and /speckit.* command references
  * inline code spans (`...`) as a multiset
  * fenced code block count/languages and heading count per level

Docs pairs are additionally checked for:
  * identical fenced code block contents (in order) and <code> spans
  * identical link/image targets, after mapping docs/vi/X back to docs/X
  * identical heading level sequence
  * every link anchor (#...) resolving to an id or heading in the target page,
    and every anchor id of the English page still existing in the Vietnamese page
The translator banner between BANNER_START/BANNER_END is ignored.

Usage: python presets/vi/tools/check_translation.py [--repo PATH] [--only preset|docs]
Exit code 0 when every pair matches, 1 otherwise.
"""
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

TRANSLATABLE_FM_KEYS = {"description", "label", "prompt", "argument-hint"}

# Inline code spans that are user-facing output text (not identifiers) and are
# intentionally translated. Every other inline code span must stay identical.
INLINE_TRANSLATIONS = {
    "**Question:**": "**Câu hỏi:**",
    "Acceptance device/runtime matrix (FR-023)": "Ma trận thiết bị/runtime để nghiệm thu (FR-023)",
    "**Question:** <interrogative>?": "**Câu hỏi:** <câu hỏi>?",
    "**Question:** <interrogative>? (FR-023)": "**Câu hỏi:** <câu hỏi>? (FR-023)",
    "**Recommended:** Option [X] - <reasoning>": "**Đề xuất:** Phương án [X] - <lý do>",
    'You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer.':
        'Bạn có thể trả lời bằng chữ cái của phương án (ví dụ "A"), đồng ý với đề xuất bằng cách trả lời "có" hoặc "đề xuất", hoặc tự đưa ra câu trả lời ngắn.',
    "**Suggested:** <your proposed answer> - <brief reasoning>": "**Gợi ý:** <câu trả lời bạn đề xuất> - <lý do ngắn gọn>",
    'Format: Short answer (<=5 words). You can accept the suggestion by saying "yes" or "suggested", or provide your own answer.':
        'Định dạng: Câu trả lời ngắn (<=5 từ). Bạn có thể đồng ý với gợi ý bằng cách trả lời "có" hoặc "gợi ý", hoặc tự đưa ra câu trả lời.',
    "## Clarifications": "## Làm rõ",
    "### Session YYYY-MM-DD": "### Phiên YYYY-MM-DD",
    "- Q: <question> → A: <final answer>": "- Hỏi: <câu hỏi> → Đáp: <câu trả lời cuối cùng>",
    '(formerly referred to as "X")': '(trước đây gọi là "X")',
    "## Phase N: Convergence": "## Giai đoạn N: Hội tụ",
    "[Spec §X.Y]": "[Đặc tả §X.Y]",
    "[Gap]": "[Thiếu]",
    "[Ambiguity]": "[Mơ hồ]",
    "[Conflict]": "[Xung đột]",
    "[Assumption]": "[Giả định]",
}

PATTERNS = {
    "speckit_placeholder": re.compile(r"__[A-Z][A-Z0-9_]*__"),
    "dollar_var": re.compile(r"\$[A-Z][A-Z0-9_]+"),
    "brace_token": re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}"),
    "caps_bracket": re.compile(r"\[[A-Z][A-Z0-9_ #-]*[A-Z0-9#]\]|\[[A-Z]\]"),
    "needs_clarification": re.compile(r"NEEDS CLARIFICATION"),
    "command_ref": re.compile(r"/?speckit[.-][a-z][a-z0-9.-]*[a-z0-9]"),
}
INLINE_CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
FENCE = re.compile(r"^[ \t]*(```+|~~~+)[ \t]*([^\s`]*)", re.M)
HEADING = re.compile(r"^(#{1,6})\s", re.M)
HEADING_LINE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
EXPLICIT_ID = re.compile(r'<a\s+id="([^"]+)"\s*>\s*</a>')
HTML_CODE = re.compile(r"<code>(.*?)</code>")
LINK_MD = re.compile(r"!?\[(?:[^\]\[]|\[[^\]]*\])*\]\(([^)\s]+)\)")
LINK_HTML = re.compile(r'(?:href|src)="([^"]+)"')
BANNER_START = "<!-- vi-banner:start -->"
BANNER_END = "<!-- vi-banner:end -->"


def split_frontmatter(text: str):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if m:
            return yaml.safe_load(m.group(1)) or {}, text[m.end():]
    return None, text


def mask_fm(obj):
    if isinstance(obj, dict):
        return {k: ("<text>" if k in TRANSLATABLE_FM_KEYS else mask_fm(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [mask_fm(v) for v in obj]
    return obj


def strip_fences(body: str) -> str:
    """Remove fenced blocks so inline-code detection is not confused."""
    out, in_fence = [], False
    for line in body.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def headings(body: str) -> Counter:
    return Counter(len(h) for h in HEADING.findall(strip_fences(body)))


def compare(en_path: Path, vi_path: Path) -> list[str]:
    errors: list[str] = []
    en, vi = en_path.read_text(encoding="utf-8"), vi_path.read_text(encoding="utf-8")
    en_fm, en_body = split_frontmatter(en)
    vi_fm, vi_body = split_frontmatter(vi)
    if mask_fm(en_fm) != mask_fm(vi_fm):
        errors.append(f"frontmatter differs:\n    en={mask_fm(en_fm)}\n    vi={mask_fm(vi_fm)}")
    for name, pat in PATTERNS.items():
        a, b = Counter(pat.findall(en_body)), Counter(pat.findall(vi_body))
        if a != b:
            errors.append(f"{name}: missing={dict(a - b)} extra={dict(b - a)}")
    a = Counter(INLINE_TRANSLATIONS.get(x, x) for x in INLINE_CODE.findall(strip_fences(en_body)))
    b = Counter(INLINE_CODE.findall(strip_fences(vi_body)))
    if a != b:
        errors.append(f"inline code: missing={dict(a - b)} extra={dict(b - a)}")
    fa, fb = FENCE.findall(en_body), FENCE.findall(vi_body)
    if len(fa) != len(fb) or [x[1] for x in fa] != [x[1] for x in fb]:
        errors.append(f"fenced blocks differ: en={len(fa)} {[x[1] for x in fa]} vi={len(fb)} {[x[1] for x in fb]}")
    if headings(en_body) != headings(vi_body):
        errors.append(f"heading levels differ: en={dict(headings(en_body))} vi={dict(headings(vi_body))}")
    return errors


def slugify(text: str) -> str:
    """GitHub-style heading id (as generated by GitHub and DocFX/markdig)."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("**", "").replace("*", "")
    out = []
    for ch in text.strip().lower():
        if ch.isalnum() or ch in "_-":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
    return "".join(out)


def strip_banner(text: str) -> str:
    return re.sub(re.escape(BANNER_START) + r".*?" + re.escape(BANNER_END) + r"\n?", "", text, flags=re.S)


def heading_records(text: str) -> list[dict]:
    """Headings outside fences, with explicit <a id> anchors directly above them."""
    recs, in_fence, pending, seen = [], False, [], Counter()
    for i, line in enumerate(text.split("\n")):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            pending = []
            continue
        if in_fence:
            continue
        ids = EXPLICIT_ID.findall(line)
        if ids and EXPLICIT_ID.sub("", line).strip() == "":
            pending += ids
            continue
        m = HEADING_LINE.match(line)
        if m:
            base = slugify(m.group(2))
            slug = base if not seen[base] else f"{base}-{seen[base]}"
            seen[base] += 1
            recs.append({"line": i, "level": len(m.group(1)), "slug": slug, "explicit": pending})
            pending = []
        elif line.strip():
            pending = []
    return recs


def anchor_ids(text: str) -> set[str]:
    ids = set(EXPLICIT_ID.findall(strip_fences(text)))
    ids |= set(re.findall(r'\bid="([^"]+)"', strip_fences(text)))
    for h in heading_records(text):
        ids.add(h["slug"])
    return ids


def fenced_blocks(text: str) -> list[str]:
    blocks, cur, fence = [], None, None
    for line in text.split("\n"):
        m = re.match(r"^\s*(```+|~~~+)", line)
        if cur is None and m:
            cur, fence = [line.strip()], m.group(1)
        elif cur is not None:
            if line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
                blocks.append("\n".join(cur + [line.strip()]))
                cur = None
            else:
                cur.append(line)
    return blocks


def link_targets(text: str) -> list[str]:
    body = strip_fences(text)
    body = INLINE_CODE.sub("", body)
    return LINK_MD.findall(body) + LINK_HTML.findall(body)


def resolve(target: str, page: str) -> tuple[str, str]:
    """Return (docs-relative path or URL, fragment) for a link on docs page *page*."""
    if re.match(r"^[a-z]+:", target):
        return target, ""
    path, _, frag = target.partition("#")
    if not path:
        return page, frag
    return posixpath.normpath(posixpath.join(posixpath.dirname(page), path)), frag


def compare_docs(repo: Path, en_path: Path, vi_path: Path) -> list[str]:
    errors: list[str] = []
    docs = repo / "docs"
    en = en_path.read_text(encoding="utf-8")
    vi = strip_banner(vi_path.read_text(encoding="utf-8"))
    if BANNER_START not in vi_path.read_text(encoding="utf-8"):
        errors.append("translator banner missing")
    en_t, vi_t = EXPLICIT_ID.sub("", en), EXPLICIT_ID.sub("", vi)
    for name, pat in PATTERNS.items():
        a, b = Counter(pat.findall(en_t)), Counter(pat.findall(vi_t))
        if a != b:
            errors.append(f"{name}: missing={dict(a - b)} extra={dict(b - a)}")
    a = Counter(INLINE_CODE.findall(strip_fences(en)) + HTML_CODE.findall(strip_fences(en)))
    b = Counter(INLINE_CODE.findall(strip_fences(vi)) + HTML_CODE.findall(strip_fences(vi)))
    if a != b:
        errors.append(f"inline code: missing={dict(a - b)} extra={dict(b - a)}")
    fa, fb = fenced_blocks(en), fenced_blocks(vi)
    if fa != fb:
        diff = next((i for i, (x, y) in enumerate(zip(fa, fb)) if x != y), min(len(fa), len(fb)))
        errors.append(f"fenced code blocks differ (en={len(fa)}, vi={len(fb)}, first difference at block {diff + 1})")
    la = [h["level"] for h in heading_records(en)]
    lb = [h["level"] for h in heading_records(vi)]
    if la != lb:
        errors.append(f"heading sequence differs: en={la} vi={lb}")
    en_page = en_path.relative_to(docs).as_posix()
    vi_page = vi_path.relative_to(docs).as_posix()

    def to_en(path: str) -> str:
        return path[3:] if path.startswith("vi/") and (docs / path).exists() else path

    ra = Counter(resolve(t, en_page) for t in link_targets(en))
    rb = Counter((to_en(p), f) for p, f in (resolve(t, vi_page) for t in link_targets(vi)))
    if ra != rb:
        errors.append(f"links: missing={dict(ra - rb)} extra={dict(rb - ra)}")
    for t in link_targets(vi):
        path, frag = resolve(t, vi_page)
        if re.match(r"^[a-z]+:", path):
            continue
        target = docs / path
        if not target.exists() and not (repo / path).exists() and not path.startswith(".."):
            errors.append(f"broken link {t} -> docs/{path}")
            continue
        if frag and target.exists() and target.suffix == ".md":
            if frag not in anchor_ids(target.read_text(encoding="utf-8")):
                errors.append(f"anchor #{frag} not found in docs/{path}")
    missing_ids = anchor_ids(en) - anchor_ids(vi)
    if missing_ids:
        errors.append(f"English anchors missing in Vietnamese page: {sorted(missing_ids)}")
    return errors


def docs_pairs(repo: Path):
    vi_docs = repo / "docs" / "vi"
    for p in sorted(vi_docs.rglob("*.md")):
        if p.name == "GLOSSARY.md":
            continue
        yield repo / "docs" / p.relative_to(vi_docs), p


def pairs(repo: Path):
    vi = repo / "presets" / "vi"
    for p in sorted((vi / "templates").glob("*.md")):
        yield repo / "templates" / p.name, p
    for p in sorted((vi / "commands").glob("speckit.*.md")):
        yield repo / "templates" / "commands" / (p.name[len("speckit."):]), p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=Path(__file__).resolve().parents[3], type=Path)
    ap.add_argument("--only", choices=["preset", "docs"])
    args = ap.parse_args()
    failed = 0
    checked = 0
    jobs = []
    if args.only != "docs":
        jobs += [(en, vi, compare) for en, vi in pairs(args.repo)]
    if args.only != "preset":
        jobs += [(en, vi, lambda e, v: compare_docs(args.repo, e, v)) for en, vi in docs_pairs(args.repo)]
    for en, vi, fn in jobs:
        checked += 1
        if not en.exists():
            print(f"FAIL {vi.relative_to(args.repo)}: no English counterpart {en}")
            failed += 1
            continue
        errs = fn(en, vi)
        rel = vi.relative_to(args.repo)
        if errs:
            failed += 1
            print(f"FAIL {rel}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"OK   {rel}")
    print(f"\n{checked - failed}/{checked} files match")
    return 1 if failed or not checked else 0


if __name__ == "__main__":
    sys.exit(main())
