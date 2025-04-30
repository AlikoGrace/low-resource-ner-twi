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
| PER  | Person        | Names of real or fictional people. Full names or referential expressions.  |
| ORG  | Organization  | Named groups like schools, institutions, military units, political bodies. |
| LOC  | Location      | Geographic or story-specific places: cities, rivers, compounds.            |
| DATE | Date/Time     | Specific dates or time expressions: years, months, relative times.         |
| MISC | Miscellaneous | Named entities not covered above, e.g., cultural objects, languages.       |

---

## Detailed Guidelines

### PER (Person)

- **Include:**

  - Full names: `Kwaku Ananse`, `Nana Ama`
  - Titles **with** names: `Nana Osei`, `Queen Abena`
  - Fictional or mythological names: `Ananse`, `Kwaku Bonsam`
  - **Context-specific referential phrases**:
    - Noun phrases pointing to specific individuals in the story:  
      `the king`, `his wife`, `the children’s grandmother`, `the old man`, etc.

- **Exclude:**
  - Generic references to people or groups: `nnipa`, `nkɔmɔfoɔ`
  - Titles alone without clear referents: `Nana`

> ✅ _Example_:  
> “Ɔkɔɔ **ɔhene no** nkyɛn.” → `ɔhene no` = B-PER  
> “Ɔne **ne yere no** kɔɔ afahyɛ no.” → `ne yere no` = B-PER

---

### ORG (Organization)

- **Include:**

  - Named traditional units: `Asafo`, `Adɔnten`, `Benkum`
  - Schools: `Achimota School`
  - Religious and political bodies: `NDC`, `Roman Catholic`

- Treat traditional regiments as organizations **if** they function like structured groups.

---

### LOC (Location)

- **Include:**

  - Towns, cities, countries: `Kumasi`, `Ghana`, `Denkyira`
  - Natural landmarks: `Pra River`, `Akuapem Mountains`
  - Regions: `Eastern Region`, `Northern Ghana`
  - **Specific story-based places**:
    - `his kitchen`, `the palace`, `their compound`, etc., **only when** the reference points to a concrete, identifiable location in the story.

- **Exclude:**
  - Generic directions: `nifa`, `benkum`, unless used in a named context.

> ✅ _Example_:  
> “Ɔsan kɔɔ **ne dan no** mu.” → `ne dan no` = B-LOC  
> “Ɔtenaa **abɔnten no** akyirikyiri.” → `abɔnten no` = B-LOC (if location is specific)

---

### DATE (Date/Time)

- **Include:**

  - Specific years and months: `1997`, `June`, `last year`, `this evening`
  - Story-time markers: `one day`, `during the festival`, `in the past`

- **Tag all time-related phrases as DATE**, even when approximate.

---

### MISC (Miscellaneous)

- **Include:**

  - Named languages: `Twi`, `Ewe`
  - Ethnic and cultural groups: `Ashanti`, `Fante`
  - Named cultural concepts or items **not fitting others**: e.g., `Abɔfra` (if a named group)

- Use this only when the entity clearly doesn’t belong to PER, ORG, LOC, or DATE.

---

## Examples

| Word/Phrase    | Entity Type | Reason                               |
| -------------- | ----------- | ------------------------------------ |
| `Kwaku Ananse` | PER         | Named character                      |
| `ɔhene no`     | PER         | Refers to a specific king in context |
| `ne yere no`   | PER         | Specific referent: his wife          |
| `Asraafokuo`   | ORG         | Traditional military group           |
| `Denkyira`     | LOC         | Geographic location                  |
| `ne dan no`    | LOC         | Specific location in story           |
| `ɛda koro bi`  | DATE        | Temporal marker                      |
| `Ashanti`      | MISC        | Ethnic label                         |

---

## Edge Cases & Clarifications

- **Referential person nouns** like “the king” or “his wife” should be annotated as PER **only when** they refer to a consistent character in the narrative.
- **Story-specific places** like “his kitchen”, “their house”, or “the palace” can be tagged LOC if they are grounded in the setting.
- **Relative Directions** (`nifa`, `benkum`) → ORG only when used in traditional group names.
- **Vague references** (like `ɔbarima bi`) are not annotated unless clearly identifiable.

---

## Format

Annotations follow **CoNLL-2003 format**, using BIO tagging (`B-PER`, `I-ORG`, etc.) for sequence labeling.

---

## Notes for Annotators

- Be consistent across files — same entity, same tag.
- Don’t over-annotate. Focus on **named or referentially-grounded** entities.
- Use comments for uncertain cases. Linguistic ambiguity is expected — just document it.

---

## Contributions

All external annotations are welcome but must follow these guidelines and will be reviewed for consistency. If contributing, **please include a changelog or comment log**.
