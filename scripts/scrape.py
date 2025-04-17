
import requests
from bs4 import BeautifulSoup
import os

URL = "https://worldstories.org.uk/reader/kweku-anansi-and-his-new-wife/akan/490"

output_path = "../data/raw/anansi_twi_story.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

story_divs=soup.find_all("div", {"class":"comment"})


for div in story_divs:
    paragraphs = div.find_all("p")
    for p in paragraphs:
        print(p.get_text(strip=True))

with open(output_path, "w", encoding="utf-8") as f:
    for para in paragraphs:
        text = para.get_text(strip=True)
        if text:
            f.write(text + "\n")

print(f" Story saved to: {output_path}")     


