import os
import requests
from bs4 import BeautifulSoup



def scrap():
    url = f"https://codeforces.com/profile/mukeremali"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find("div", class_="_UserActivityFrame_counterValue")

    score = score_element.text.strip() if score_element else "N/A"
    rank = ''
    absolute_logo_url = "../../media/scrape/codeforces.png"
    name = "Codeforces"
    return name, absolute_logo_url,score, rank

# Usage
