import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

print("📌 Scraped Quotes:\n")

for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")
