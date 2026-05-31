import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://quotes.toscrape.com"

url = base_url

data = []

while url:

    print("Scraping:", url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        data.append({
            "Quote": text,
            "Author": author
        })

    # Find next button
    next_btn = soup.find("li", class_="next")

    if next_btn:
        next_page = next_btn.find("a")["href"]
        url = base_url + next_page
    else:
        url = None

# Save CSV
df = pd.DataFrame(data)

df.to_csv("all_quotes.csv", index=False)

print("All pages scraped successfully")