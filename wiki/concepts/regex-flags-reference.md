---
type: concept
tags: [regex, python, pattern-matching, string-parsing, text-processing]
sources: ["Python re documentation"]
updated: 2026-11-20
---

# Regular Expression Flags Reference

Regular expression flags alter the parsing, anchoring, and character-matching semantics of pattern-matching engines. In Python, flags can be passed programmatically to functions in the `re` module or specified directly inside pattern strings using inline modifier syntax.

## Core Regex Flags

| Inline Flag | Python `re` Constant | Name | Description & Semantic Impact |
| :--- | :--- | :--- | :--- |
| `(?m)` | `re.M` / `re.MULTILINE` | **Multiline** | Changes the behavior of `^` and `$` anchors. By default, `^` and `$` match only the start and end of the entire string. In multiline mode, `^` matches the beginning of each line (after `\n`), and `$` matches the end of each line (before `\n`). |
| `(?i)` | `re.I` / `re.IGNORECASE` | **Ignore Case** | Enables case-insensitive matching. Letters match regardless of casing (e.g., `test` matches `test`, `Test`, and `TEST`). |
| `(?s)` | `re.S` / `re.DOTALL` | **Dot-All** | Modifies the dot `.` metacharacter. By default, `.` matches any character except newline `\n`. With dot-all active, `.` matches any character whatsoever, including line terminators. |

## Essential Modifiers & Assertions

### Lookaround Assertions
- **Positive Lookahead `(?=...)`**: Asserts that the subpattern matches immediately after the current position without advancing the match pointer (zero-width assertion).
  - *Example*: Splitting blocks without removing delimiter headers: `re.split(r"(?m)(?=^Question\s+\d+)", text)`.
- **Negative Lookahead `(?!...)`**: Asserts that the subpattern does *not* match immediately following the current position.

### End of String Anchor (`\Z`)
- While `$` in multiline mode matches before every newline, `\Z` always matches strictly at the absolute end of the input string or before an ultimate terminal newline. It provides an unambiguous boundary when validating full document buffers.

## Practical Example in Python
```python
import re

text = """Question 1: What is Python?
A programming language.
Question 2: What is regex?
Pattern matching syntax."""

# Multiline + Dotall pattern to extract blocks
pattern = re.compile(r"^Question\s+(\d+):\s*(.+?)(?=\nQuestion|\Z)", re.MULTILINE | re.DOTALL)
matches = pattern.findall(text)
```

## References
- Usage in Data Pipelines: [[data-cleaning-guide]]
