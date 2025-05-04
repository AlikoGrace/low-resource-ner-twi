import os


def normalize_datetime_tags(text):
    text = text.replace("B-DATE/TIME", "B-DATE").replace("I-DATE/TIME", "I-DATE")
    text = text.replace("B-TIME", "B-DATE").replace("I-TIME", "I-DATE")
    return text


def fix_io_labels(text):
    return text.replace("I-O", "O")



def fix_bare_entity_tags(text):
    entity_types = ["PER", "ORG", "LOC", "DATE", "MISC"]

    lines = text.splitlines()
    fixed_lines = []

    for line in lines:
        if not line.strip():
            fixed_lines.append("") 
            continue

        parts = line.split()
        if len(parts) != 2:
            fixed_lines.append(line)
            continue

        token, label = parts

       
        if label in entity_types:
            label = f"B-{label}"

        fixed_lines.append(f"{token} {label}")

    return "\n".join(fixed_lines)



def clean_labels(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    text = normalize_datetime_tags(text)
    text = fix_io_labels(text)
    text = fix_bare_entity_tags(text)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)


# def run_all_fixes(base_dir):
#     for file in ["train.conll", "dev.conll", "test.conll"]:
#         path = os.path.join(base_dir, file)
#         clean_labels(path)
#     print("All label fixes applied.")

if __name__ == "__main__":
    clean_labels("data/processed/cleaned_combined_ner_dataset.conll")
    print("Label fixes applied to cleaned_combined_ner_dataset.conll")

