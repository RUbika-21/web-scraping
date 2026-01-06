import requests
from bs4 import BeautifulSoup
import pandas as pd

all_data = []

base_url = "http://quotes.toscrape.com/page/"

for page in range(1, 6):  # scrape 5 pages
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.find_all("div", class_="quote"):
        quote = item.find("span", class_="text").text
        author = item.find("small", class_="author").text
        tags = [tag.text for tag in item.find_all("a", class_="tag")]

        all_data.append({
            "quote": quote,
            "author": author,
            "tags": ", ".join(tags)
        })

df = pd.DataFrame(all_data)
df.to_excel("quotes_dataset.xlsx", index=False)

print("MULTI-PAGE DATASET CREATED")
