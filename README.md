# Low-resource Named Entity Recognition (NER) for Twi Language

**Project Overview**

This project aims to develop a robust Named Entity Recognition (NER) system for the Twi language, a low-resource African language with limited labeled data. By addressing the challenges faced by languages with scarce linguistic resources, this initiative contributes to creating scalable, linguistically-informed NLP models for African languages. The project involves data scraping, manual data collection, annotation, model training, and a multilingual baseline approach for African languages.

---

## Key Objectives

- **Low-resource NER System:** Build a Twi NER system with core entity types: PER, LOC, ORG, DATE,MISC.
- **Data Collection & Annotation:** Combine scraping, manual curation, and labeling with clear guidelines.
- **Multilingual Baseline:** Experiment with cross-lingual transfer for African language NER.
- **Open-source Contribution:** Offer high-quality, reproducible resources for the research community.

---

## Project Structure

```
low-resource-ner-twi/
│
├── data/
│   ├── raw/                         # Raw text data (scraped or collected)
│   ├── processed/                   # CoNLL files and sentence-level preprocessed data
│   └── README.md                    # Notes on data sources and structure
│
├── scripts/
│   ├── scrape.py                    # Scraping logic for story/paper content
│   ├── split_into_sentences.py     # Sentence segmentation for annotation prep
│   ├── count_entities.py           # Entity/statistics summarizer from .conll
│   └── utils.py                     # Helper functions
│
├── docs/
│   ├── annotation_guide.md         # Entity labeling guidelines
│   └── research_notes.md           # Observations and notes from annotation + modeling
│
├── notebooks/                      # Jupyter notebooks for exploration and model training
│
├── models/                         # Saved model checkpoints or training configs
│
├── requirements.txt
└── README.md                       # This file
```

---

## Data Collection

We use both automatically scraped and manually curated sources including:

- **Stories** (e.g., folklore texts, public domain content)
- **Academic Papers** (especially culturally grounded material)

### Example Sources

- [World Stories - Anansi](https://worldstories.org.uk/reader/kweku-anansi-and-his-new-wife/akan/490)
- [Academia.edu - Akan Anansesem](https://www.academia.edu/96287748/Akan_Ananses%C9%9Bm_Ab%C9%9Bn_a_%C9%9Bgyee_Ananse_nkwa_no)

---

## Annotation

- Tool: **Label Studio**
- Format: CoNLL-2003
- Annotated Entity Types:

| Label | Meaning                | Examples                             |
| ----- | ---------------------- | ------------------------------------ |
| PER   | Person names           | Kofi, Nana Ama, Ananse               |
| LOC   | Geographical locations | Accra, Lake Bosomtwe, Eastern Region |
| ORG   | Groups or institutions | Asraafokuo, Parliament, GES          |
| DATE  | Time expressions       | 1997, today, last year               |
| MISC  | Other Meaningful but   | Festive names, mythological figures  |
|       | uncategorized entities | etc                                  |
|       | PER/ORG/LOC            |                                      |

Full guidelines: [docs/annotation_guide.md](docs/annotation_guide.md)

---

## Model Training

Will be updated soon.

## Multilingual Focus

This project is designed with transferability in mind: annotated data and training code will serve as a base for future work on related African languages.

---

## Setup & Usage

```bash
# Clone the repo
git clone https://github.com/AlikoGrace/low-resource-ner-twi.git
cd low-resource-ner-twi

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Contributing

Contributions and discussions are welcome — whether you’re a linguist, researcher, or developer.

How to contribute:

1. Fork this repo
2. Create a branch
3. Make your changes
4. Submit a PR

---

## License

MIT License — feel free to use, modify, and share with attribution.

---

## Contact

For questions or collaboration ideas, feel free to open an issue or reach out via Email [gracealiko10@gmail.com].
