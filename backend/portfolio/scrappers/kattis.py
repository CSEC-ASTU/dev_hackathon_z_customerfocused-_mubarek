import os
import requests
from bs4 import BeautifulSoup



def scrap():
    url = f"https://open.kattis.com/users/mukerem"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all("span", class_="important_number")[1]
    rank_element = soup.find_all("span", class_="important_number")[0]

    score = score_element.text.strip() if score_element else "N/A"
    rank = rank_element.text.strip() if rank_element else "N/A"
    absolute_logo_url = "../../media/scrape/kattis.png"

    name = "Kattis"
    return name, absolute_logo_url,score, rank

# Usage
