import os

def extract_labels(filepath):
    labels = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split()
                if len(parts) == 2:
                    token, label = parts
                    labels.add(label)
    return labels

def compare_label_sets(file1, file2):
    labels1 = extract_labels(file1)
    labels2 = extract_labels(file2)

    print(f"\nLabels in {os.path.basename(file1)}:")
    print(sorted(labels1))
    
    print(f"\nLabels in {os.path.basename(file2)}:")
    print(sorted(labels2))

    print("\n--- Comparison ---")
    print("✅ Common labels:")
    print(sorted(labels1 & labels2))

    print("\n⚠️ Labels in file1 not in file2:")
    print(sorted(labels1 - labels2))

    print("\n⚠️ Labels in file2 not in file1:")
    print(sorted(labels2 - labels1))

if __name__ == "__main__":
    file1 = "../data/processed/final.conll"
    file2 = "../data/masakha/masakha.conll"

    compare_label_sets(file1, file2)
