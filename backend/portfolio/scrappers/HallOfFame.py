import os
import requests
from bs4 import BeautifulSoup



def scrap():
    url = f"https://cphof.org/profile/codeforces:mukeremali"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    points_element = soup.find_all("td", class_="light-cell")[-1]
    points_elements = soup.find_all("td", class_="light-cell")[0]
    score = points_element.text.strip() if points_element else "N/A"
    rank = ''

    absolute_logo_url = "../../media/scrape/halloffame.png"
    name = "Hall of Fame"
    return name, absolute_logo_url,score, rank

# Usage
