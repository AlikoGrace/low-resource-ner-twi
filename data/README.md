# Data Folder

This folder contains raw and processed data files used for building a low-resource Named Entity Recognition (NER) dataset for the Twi language.

## Folder Structure

- `raw/` – Contains unprocessed text data scraped from stories, news, and traditional archives. **Not included in the repository** due to copyright and size concerns.
- `processed/` – Contains annotated and sentence-split `.conll` files used to train and evaluate the NER model.

## Notes

- Only a sample of processed data is included here. The full dataset will be released separately on [Kaggle/Hugging Face] when the project is published.
- If you are contributing or extending this dataset, please follow the annotation guidelines provided in the root `annotations_guide.md` file.
<!-- - Approximately 300 annotated sentences are being prepared as part of this dataset. This number is sufficient to train a multilingual baseline model for low-resource language experimentation. -->

## Format

All processed data files are in CoNLL format with the following entity types:

- `PER`: Person
- `ORG`: Organization
- `LOC`: Location
- `DATE/TIME`: Temporal expressions (dates and time)
- `MISC`: Named entities that don't fall into the above categories

Each sentence is separated by a blank line.

---

> **Note:** Some files were manually corrected for spelling and spacing before annotation.

## Limitations

- Data is from varied domains (folklore, news, etc.) and may not be balanced.
- Some files are partially annotated.
- Encoding: All files are UTF-8.

## Licensing / Attribution

- **Scraped Data**: Used for academic and research purposes under fair use.
- **Manual Transcripts**: Created by the project author.
- **Original stories**: Credits in citation docs.

Please contact [Grace Aliko](https://github.com/AlikoGrace) for reuse permissions or further questions.
