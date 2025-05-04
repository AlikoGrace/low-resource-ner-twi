import argparse
import re


def fix_lowercase_o_tags(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^[^\s]+\so$", stripped):
            token = stripped.split()[0]
            fixed_lines.append(f"{token} O\n")
        else:
            fixed_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)

    print(f" Fixed lowercase 'o' tags written to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix lowercase 'o' tags in CoNLL files.")
    parser.add_argument("input", help="Path to input .conll file")
    parser.add_argument("output", help="Path to output .conll file (fixed)")

    args = parser.parse_args()
    fix_lowercase_o_tags(args.input, args.output)
