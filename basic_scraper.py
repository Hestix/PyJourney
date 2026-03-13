import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

for i, title in enumerate(titles, start=1):
    print(f"{i}. {title.text}")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(title.text + "\n")