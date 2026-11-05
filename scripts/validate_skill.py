#!/usr/bin/env python3
"""validate_skill.py — minimal structural validator for a built business skill folder.

Implements the machine-checkable part of this repo's validation checklist:
  errors (exit 1):
    - SKILL.md missing
    - frontmatter missing, or lacking name: / description:
    - a relative link in SKILL.md points to a file that does not exist
    - references/ missing or empty (a business skill must carry its rules somewhere)
  warnings (exit 0):
    - no agent-boundary language found (method step 3: may / must-never / escalate)
    - no validation material found (method step 6: a validation checklist
      reference or validation cases)

Usage: python3 scripts/validate_skill.py <skill-folder>
Output: one JSON object {folder, errors, warnings}. Pure stdlib.
"""
import json, os, re, sys

BOUNDARY_WORDS = ['escalat', 'must never', 'must not', 'never ', 'boundary', 'approval', 'human review']
VALIDATION_WORDS = ['validation', 'test case', 'test-case', 'acceptance']

def main():
    if len(sys.argv) != 2:
        print(json.dumps({'error': 'usage: validate_skill.py <skill-folder>'})); return 2
    folder = sys.argv[1]
    errors, warnings = [], []
    skill_md = os.path.join(folder, 'SKILL.md')
    if not os.path.isfile(skill_md):
        print(json.dumps({'folder': folder, 'errors': ['SKILL.md missing'], 'warnings': []}, ensure_ascii=False, indent=1)); return 1
    text = open(skill_md, encoding='utf-8').read()

    # frontmatter
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        errors.append('SKILL.md has no YAML frontmatter')
    else:
        fm = m.group(1)
        if not re.search(r'^name\s*:', fm, re.M): errors.append('frontmatter lacks name:')
        if not re.search(r'^description\s*:', fm, re.M): errors.append('frontmatter lacks description:')

    # relative links resolve
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if link.startswith(('http://', 'https://', '#', 'mailto:')): continue
        target = link.split('#')[0]
        if target and not os.path.exists(os.path.join(folder, target)):
            errors.append(f'broken link in SKILL.md: {link}')

    # references present
    refs = os.path.join(folder, 'references')
    if not (os.path.isdir(refs) and any(os.scandir(refs))):
        errors.append('references/ missing or empty')

    low = text.lower()
    if not any(w in low for w in BOUNDARY_WORDS):
        warnings.append('no agent-boundary language found (method step 3: define may / must-never / escalate before build)')
    has_val_file = os.path.isfile(os.path.join(refs, 'validation-checklist.md')) if os.path.isdir(refs) else False
    if not has_val_file and not any(w in low for w in VALIDATION_WORDS):
        warnings.append('no validation material found (method step 6: validate against real cases before release)')

    print(json.dumps({'folder': folder, 'errors': errors, 'warnings': warnings}, ensure_ascii=False, indent=1))
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
