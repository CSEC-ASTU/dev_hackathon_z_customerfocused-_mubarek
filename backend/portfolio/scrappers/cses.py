import os
import requests
from bs4 import BeautifulSoup


def scrap():
    url = f"https://cses.fi/user/119282"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all("td")[1]

    score = score_element.text.strip() if score_element else "N/A"
    rank = ''
    absolute_logo_url = "../../media/scrape/cses.png"
    name = "CSES"
    return name, absolute_logo_url,score, rank


def m():
    return "man"