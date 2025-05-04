import os
import argparse
import random

def read_conll(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read().strip()
    return [s.strip() for s in content.split("\n\n") if s.strip()]

def write_conll(sentences, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sentences))
        f.write("\n")

def split_data(sentences, train_ratio=0.8, dev_ratio=0.1):
    total = len(sentences)
    train_end = int(total * train_ratio)
    dev_end = train_end + int(total * dev_ratio)

    return sentences[:train_end], sentences[train_end:dev_end], sentences[dev_end:]

def main(input_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    sentences = read_conll(input_path)
    random.shuffle(sentences)

    train, dev, test = split_data(sentences)

    write_conll(train, os.path.join(output_dir, "train.conll"))
    write_conll(dev, os.path.join(output_dir, "dev.conll"))
    write_conll(test, os.path.join(output_dir, "test.conll"))

    print(f" Done. Split {len(sentences)} sentences:")
    print(f"  • Train: {len(train)}")
    print(f"  • Dev:   {len(dev)}")
    print(f"  • Test:  {len(test)}")
    print(f"Files saved in: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to .conll file (e.g. all_trimmed.conll)")
    parser.add_argument("--outdir", default="data/split", help="Directory to save splits")
    args = parser.parse_args()

    main(args.input, args.outdir)
