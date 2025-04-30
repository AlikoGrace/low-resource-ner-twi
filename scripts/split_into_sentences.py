import re
import os
import html

file_path = "../data/raw/news3.txt"

def clean_text(text):
   
    text = html.unescape(text)
    
    
    text = re.sub(r'<[^>]+>', '', text)
    
   
    text = text.replace('\xa0', ' ')  
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def split_into_sentences(text):
    text = clean_text(text)

    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

sentences = split_into_sentences(text)


input_directory = os.path.dirname(file_path)
input_filename = os.path.basename(file_path)
output_filename = os.path.splitext(input_filename)[0] + "_sentences" + os.path.splitext(input_filename)[1]
output_path = os.path.join(input_directory, output_filename)


with open(output_path, "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence.strip() + "\n")

print(f"Sentences saved to: {output_path}")
