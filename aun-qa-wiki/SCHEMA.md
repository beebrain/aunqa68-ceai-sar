# Wiki Schema

## Domain
AUN-QA (ASEAN University Network - Quality Assurance) — ระบบประกันคุณภาพสำหรับสถาบันอุดมศึกษาไทย ครอบคลุมหลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ มหาวิทยาลัยสงเคราะห์

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `clo-specification.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source.
- Language: Thai content with English technical terms in parentheses where appropriate
- Code examples or technical terms in `code` format

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true | false
contradictions: [other-page-slug]
---
```

## Tag Taxonomy
- Quality: aun-qa, accreditation, standard, criteria, indicator
- Curriculum: program, clo, plo, course, mapping
- Documentation: report, proposal, evidence, compliance
- Process: self-assessment, external-review, improvement
- Organization: university, faculty, department, committee
- Document-Type: specification, guideline, template, manual

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines

## Entity Pages
- One page per notable entity (university, program, committee)
- Include: overview, key facts, relationships

## Concept Pages
- One page per concept (criteria, indicator, standard)
- Include: definition, current requirements, examples

## Comparison Pages
- Side-by-side analyses of similar entities or standards

## Update Policy
When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older
2. Note both positions with dates and sources if contradictory
3. Mark contradiction in frontmatter: `contradictions: [page-name]`