import os

input_files = [
    "../data/processed/ananse_story1_annotated.conll",
    "../data/processed/ananse_story2_annotated.conll",
    "../data/processed/story3_annotated.conll",
    "../data/processed/news1_annotated.conll",
    "../data/processed/news2_annotated.conll"
]
output_file = "../data/processed/combined_ner_dataset.conll"

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w", encoding="utf-8") as outfile:
    for fname in input_files:
        if not os.path.isfile(fname):
            print(f" File not found: {fname}")
            continue

        print(f" Adding {fname}")
        with open(fname, "r", encoding="utf-8") as infile:
            contents = infile.read().strip()
            outfile.write(contents + "\n\n") 

print(f"\n Combined dataset saved to: {output_file}")
