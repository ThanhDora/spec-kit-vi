#!/usr/bin/env python3
"""Check that the Vietnamese preset keeps every machine-relevant token of the
English core templates/commands.

For each pair (core English file, Vietnamese preset file) it compares:
  * YAML frontmatter (all keys and values, except human-readable text fields)
  * placeholders: __SPECKIT_*__, $ARGUMENTS-style, {SCRIPT}-style, [ALL_CAPS]
  * [NEEDS CLARIFICATION] markers and /speckit.* command references
  * inline code spans (`...`) as a multiset
  * fenced code block count/languages and heading count per level

Usage: python presets/vi/tools/check_translation.py [--repo PATH]
Exit code 0 when every pair matches, 1 otherwise.
"""
from __future__ import annotations

import argparse
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


def pairs(repo: Path):
    vi = repo / "presets" / "vi"
    for p in sorted((vi / "templates").glob("*.md")):
        yield repo / "templates" / p.name, p
    for p in sorted((vi / "commands").glob("speckit.*.md")):
        yield repo / "templates" / "commands" / (p.name[len("speckit."):]), p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=Path(__file__).resolve().parents[3], type=Path)
    args = ap.parse_args()
    failed = 0
    checked = 0
    for en, vi in pairs(args.repo):
        checked += 1
        if not en.exists():
            print(f"FAIL {vi.relative_to(args.repo)}: no English counterpart {en}")
            failed += 1
            continue
        errs = compare(en, vi)
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
