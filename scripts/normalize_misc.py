def normalize_misc_labels(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    normalized = []
    for line in lines:
        if line.strip():
            parts = line.strip().split()
            if len(parts) == 2:
                token, label = parts
                if label in ["B-MISC", "I-MISC"]:
                    label = "O"
                normalized.append(f"{token} {label}")
            else:
                normalized.append(line.strip())  
        else:
            normalized.append("")  

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(normalized))

normalize_misc_labels("../data/processed/cleaned_combined_ner_dataset.conll")
print(" MISC labels normalized to O.")
