import os

def normalize_date_labels(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            line = line.replace("B-DATE/TIME", "B-DATE").replace("I-DATE/TIME", "I-DATE")
            f.write(line)

base_path = "data/split"
for split in ["train.conll", "dev.conll", "test.conll"]:
    normalize_date_labels(os.path.join(base_path, split))

print("All DATE/TIME tags normalized.")
