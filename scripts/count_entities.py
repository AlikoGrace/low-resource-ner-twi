import argparse
from collections import defaultdict

def count_entities(conll_file):
    with open(conll_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entity_counts = defaultdict(int)
    num_sentences = 0
    num_tokens = 0
    in_sentence = False
    current_sentence_tags = []
    num_o_sentences = 0

    for line in lines:
        line = line.strip()

        if not line:
            if in_sentence:
                num_sentences += 1
                if all(tag == "O" for tag in current_sentence_tags):
                    num_o_sentences += 1
                current_sentence_tags = []
                in_sentence = False
            continue

        in_sentence = True
        num_tokens += 1

        parts = line.split()
        if len(parts) >= 2:
            tag = parts[-1]
            current_sentence_tags.append(tag)
            if tag.startswith("B-") or tag.startswith("I-"):
                entity_type = tag[2:]

                # Normalize composite tags
                if entity_type == "DATE/TIME":
                    entity_type = "DATE"

                entity_counts[entity_type] += 1

    # Final sentence check (in case no trailing newline)
    if in_sentence and current_sentence_tags:
        num_sentences += 1
        if all(tag == "O" for tag in current_sentence_tags):
            num_o_sentences += 1

    print(f"\n File: {conll_file}")
    print(f" Total Sentences: {num_sentences}")
    print(f" Total Tokens: {num_tokens}")
    print(f" Sentences with only 'O' tags: {num_o_sentences}")
    
    if num_sentences > 0:
        o_sentence_pct = (num_o_sentences / num_sentences) * 100
        if o_sentence_pct > 40:
            print(f"⚠️ Warning: {o_sentence_pct:.2f}% of sentences have no entity tags. Consider balancing the dataset.\n")

    print(f"\n Entity Counts:")
    total_entities = sum(entity_counts.values())
    for ent_type in ["PER", "ORG", "LOC", "DATE", "MISC"]:
        count = entity_counts[ent_type]
        pct = (count / total_entities * 100) if total_entities > 0 else 0
        warning = "⚠️" if pct < 5 and count > 0 else ""
        print(f"{ent_type:5}: {count:4} ({pct:.2f}%) {warning}")
    
    # Print out the percentage of 'O' tag sentences
    if num_sentences > 0:
        o_percentage = (num_o_sentences / num_sentences) * 100
        print(f" 'O' sentences as percentage of total: {o_percentage:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count entities in a CoNLL file")
    parser.add_argument("--file", type=str, required=True, help="Path to the CoNLL file")
    args = parser.parse_args()

    count_entities(args.file)
