# Data Folder

This folder contains raw and processed data files used for building a low-resource Named Entity Recognition (NER) dataset for the Twi language.

## Folder Structure

- `raw/` – Contains unprocessed text data scraped from stories, news, and traditional archives. **Not included in the repository** due to copyright and size concerns.
- `processed/` – Contains annotated and sentence-split `.conll` files used to train and evaluate the NER model.

## Notes

- Only a sample of processed data is included here. The full dataset will be released separately on [Kaggle/Hugging Face] when the project is published.
- If you are contributing or extending this dataset, please follow the annotation guidelines provided in the root `annotations_guide.md` file.

## Format

All processed data files are in CoNLL format with the following entity types:

- `PER`: Person
- `ORG`: Organization
- `LOC`: Location
- `DATE`: Temporal expressions (e.g. calendar dates, absolute time references)

Each sentence is separated by a blank line.

> **Note:** All `DATE/TIME`, `TIME`, and related tags were normalized to `DATE` for consistency with the MasakhaNER Twi annotation scheme.
>
> `MISC` entity tags have been removed.

---

## Dataset Composition

- A mix of manually annotated sentences from diverse domains (folklore, news, conversations).
- Synthetic data was lightly used to improve class balance (especially for ORG/LOC).
- The combined dataset contains:
  - ~600+ sentences
  - ~13,000+ tokens
  - ~1,000+ labeled entities

> **Note:** All files are encoded in UTF-8.

---

## Limitations

- Data is from varied domains and may not be fully balanced.
- Some originally scraped or written files were partially annotated.
- Class coverage for certain entities (especially ORG) may be lower than PER or LOC.

---

## Licensing / Attribution

- **Scraped Data**: Used under academic fair use.
- **Synthetic / Manual Annotations**: Created by the project author.
- **Original stories**: See `citation_credits.md` for attributions.
- **MasakhaNER Twi Data**: Integrated and used under the Creative Commons Attribution 4.0 License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). Sourced from:

  > MasakhaNER 2.0: Named Entity Recognition for African Languages.  
  > GitHub: https://github.com/masakhane-io/masakhane-ner  
  > Dataset: https://huggingface.co/datasets/masakhaner2

---

## Contact

For questions, collaboration, or reuse permissions, contact [Grace Aliko](https://github.com/AlikoGrace).
