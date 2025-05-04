import random

def read_conll(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read().strip()

    sentences = data.split("\n\n")
    return [s.splitlines() for s in sentences]

def is_o_only(sentence_lines):
    return all(line.strip().endswith(" O") for line in sentence_lines if line.strip())

def write_conll(sentences, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for s in sentences:
            f.write("\n".join(s) + "\n\n")

def reduce_o_only_sentences(input_path, output_path, drop_pct=0.3, seed=42):
    random.seed(seed)
    sentences = read_conll(input_path)

    o_only = [s for s in sentences if is_o_only(s)]
    not_o_only = [s for s in sentences if not is_o_only(s)]

    n_drop = int(len(o_only) * drop_pct)
    print(f"Dropping {n_drop} out of {len(o_only)} 'O'-only sentences.")

    o_only_reduced = random.sample(o_only, len(o_only) - n_drop)
    final = not_o_only + o_only_reduced
    random.shuffle(final)

    write_conll(final, output_path)
    print(f"Saved reduced dataset to: {output_path}")
    print(f"Final sentence count: {len(final)}")


if __name__ == "__main__":
    reduce_o_only_sentences(
        input_path="../data/processed/all.conll",
        output_path="../data/processed/all_trimmed.conll",
        drop_pct=0.3 
    )
