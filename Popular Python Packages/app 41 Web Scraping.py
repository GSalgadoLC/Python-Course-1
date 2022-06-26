# Scraping data from websites
# Web crawler

import requests
from bs4 import BeautifulSoup


response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".flush-left")
print(type(questions[1]).attrs)
