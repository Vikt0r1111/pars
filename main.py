from bs4 import BeautifulSoup
import json
import requests

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f)

for tag_a in soup.select("h1"):
    text = tag_a.text

with open("info.txt", "w") as file:
    file.write(text)