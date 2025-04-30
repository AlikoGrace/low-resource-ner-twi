
import re

def clean_conll_format(input_path, output_path):
    cleaned_lines = []
    with open(input_path, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                cleaned_lines.append("")  
                continue

            
            match = re.match(r"^(.*?)\s+-X-\s+_\s+(.*)$", line)
            if match:
                token, tag = match.groups()
                cleaned_lines.append(f"{token} {tag}")
            else:
                print(f"Skipping malformed line: {line}")

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(cleaned_lines))




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    clean_conll_format(args.input, args.output)
