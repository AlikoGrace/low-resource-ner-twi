# Annotation Guidelines for Twi Named Entity Recognition (NER)

This document provides detailed annotation guidelines for the **Twi NER dataset** developed as part of the _Low-resource Named Entity Recognition for Twi_ project. The goal is to ensure consistency, clarity, and linguistic integrity across all annotations.

---

## Philosophy

This project is rooted in the belief that **low-resource NLP deserves high-quality linguistic care**. Twi, like many African languages, exhibits context-dependent structure, oral-leaning patterns, and culturally specific expressions. These guidelines aim to honor that by being both practical and linguistically informed.

---

## Entity Types

We use **five core entity types**, each with clear boundaries and culturally adapted examples.

| Tag  | Entity Type   | Description                                                                |
| ---- | ------------- | -------------------------------------------------------------------------- |
| PER  | Person        | Names of real or fictional people. Full names or partial names.            |
| ORG  | Organization  | Named groups like schools, institutions, military units, political bodies. |
| LOC  | Location      | Geographic locations: cities, towns, countries, rivers, landmarks.         |
| DATE | Date/Time     | Specific dates or time expressions: years, months, relative times.         |
| MISC | Miscellaneous | Named entities not covered above, e.g., cultural objects, languages.       |

---

## Detailed Guidelines

### PER (Person)

- Include:

  - First and last names: `Kwaku Ananse`, `Nana Ama`
  - Royalty, titles, if they are used **with** a name: `Nana Osei`
  - Fictional names: `Ananse`, `Kwaku Bonsam`

- Exclude:
  - Generic group references like `nkↄmↄfoↄ` or `nnipa`
  - Titles **alone**: `Nana` without a name is ignored

### ORG (Organization)

- Include:

  - Named traditional units: `Asafo`, `Adɔnten`, `Benkum`
  - Schools: `Achimota School`
  - Churches, political parties, armies: `NDC`, `Roman Catholic`

- Treat traditional regiments as organizations **if** they function like structured groups.

### LOC (Location)

- Include:

  - Towns, countries: `Kumasi`, `Ghana`, `Denkyira`
  - Rivers, landmarks: `Pra River`, `Akuapem Mountains`
  - Relative regions: `Eastern Region`, `Northern Ghana`

- Exclude:
  - Directions used generically: `nifa` (unless part of a known regional unit)

### DATE (Date/Time)

- Include:

  - Specific years/dates: `1997`, `June`, `last year`, `today`, `this evening`
  - Time periods in historical narratives: `during the festival`, `in the past`

- Combine both **date and time** into one unified DATE tag for simplicity.

### MISC (Miscellaneous)

- Include:

  - Named languages: `Twi`, `Ewe`
  - Ethnic/cultural labels: `Ashanti`, `Fante`
  - Named cultural items or groups **not fitting others**: e.g. `Abɔfra`, if referring to a named group

- Use as a **fallback** when the entity doesn’t fit cleanly into the above.

---

## Examples

| Word/Phrase    | Entity Type | Reason                          |
| -------------- | ----------- | ------------------------------- |
| `Kwaku Ananse` | PER         | Full name of a person/character |
| `Asraafokuo`   | ORG         | Named traditional group         |
| `Denkyira`     | LOC         | Town/kingdom                    |
| `in 1997`      | DATE        | Specific year                   |
| `Ashanti`      | MISC        | Ethnic/cultural label           |

---

## Edge Cases & Clarifications

- **Relative Directions** (e.g., `nifa`, `benkum`) are annotated as ORG **only** if part of a named regiment or traditional unit.
- **Colloquial time phrases** like `ɛnnɛ` (today), `nnɛ anɔpa` (this morning) → still DATE.
- If **unsure**, leave a comment in your annotation tool and tag for review.

---

## Format

Annotations are saved in **CoNLL-2003 format**, with BIO tags (`B-PER`, `I-ORG`, etc.) for sequence labeling.

---

## Notes for Annotators

- Be consistent: Always annotate the same name the same way across all files.
- Don’t over-annotate: Only tag named entities, not every noun.
- Use comments or logs if uncertain. Ambiguity is expected — it's part of the work.

---

## Contributions

We welcome contributions, but all annotations will be reviewed for consistency. Follow these guidelines strictly if contributing new labeled data.
