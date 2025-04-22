import os

# Make sure the output directory exists
os.makedirs("data/processed", exist_ok=True)

# List of annotated files to combine
input_files = [
    "data/processed/ananse_story1_annotated.conll",
    "data/processed/ananse_story2_annotated.conll",
    "data/processed/story3_annotated.conll",
    "data/processed/news1_annotated.conll",
    "data/processed/news2_annotated.conll"
]

# Output combined file
output_file = "data/processed/combined_ner_dataset.conll"

with open(output_file, "w", encoding="utf-8") as outfile:
    for fname in input_files:
        with open(fname, "r", encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)
            outfile.write("\n")  # Add newline between files

print(f"✅ Combined {len(input_files)} files into {output_file}")
