import requests
from bs4 import BeautifulSoup
import os

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

images = soup.find_all("img")

# Create folder
os.makedirs("images", exist_ok=True)

for index, image in enumerate(images):

    img_url = image["src"]

    # Fix relative URL
    img_url = "https://books.toscrape.com/" + img_url.replace("../", "")

    img_data = requests.get(img_url).content

    filename = f"images/book_{index}.jpg"

    with open(filename, "wb") as f:
        f.write(img_data)

    print("Downloaded:", filename)

print("All images downloaded")