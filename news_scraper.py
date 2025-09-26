# news_scraper.py

import requests
from bs4 import BeautifulSoup

URL = "https://edition.cnn.com/"   # You can change to any news site
OUTPUT_FILE = "headlines.txt"

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # check for errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines - (BBC example uses <h2>)
        headlines = []
        for h2 in soup.find_all("h2"):
            text = h2.get_text(strip=True)
            if text:
                headlines.append(text)

        return headlines
    except Exception as e:
        print("Error fetching headlines:", e)
        return []

def save_headlines(headlines, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, headline in enumerate(headlines, 1):
            file.write(f"{idx}. {headline}\n")

def main():
    print("Fetching news headlines...")
    headlines = fetch_headlines(URL)

    if headlines:
        save_headlines(headlines, OUTPUT_FILE)
        print(f"✅ {len(headlines)} headlines saved to {OUTPUT_FILE}")
    else:
        print("⚠️ No headlines found.")


main()
