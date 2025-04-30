import os
import random

def read_conll_sentences(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    return content.split("\n\n")

def write_sentences(sentences, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sentences))

def split_dataset(input_path, output_dir, seed=42):
    os.makedirs(output_dir, exist_ok=True)

    sentences = read_conll_sentences(input_path)
    print(f"Total sentences: {len(sentences)}")

    random.seed(seed)
    random.shuffle(sentences)

    n_total = len(sentences)
    n_train = int(n_total * 0.8)
    n_dev = int(n_total * 0.1)

    train = sentences[:n_train]
    dev = sentences[n_train:n_train + n_dev]
    test = sentences[n_train + n_dev:]

    write_sentences(train, os.path.join(output_dir, "train.conll"))
    write_sentences(dev, os.path.join(output_dir, "dev.conll"))
    write_sentences(test, os.path.join(output_dir, "test.conll"))

    print(f"Split complete: Train={len(train)}, Dev={len(dev)}, Test={len(test)}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    args = parser.parse_args()

    split_dataset(args.input, args.output_dir)
