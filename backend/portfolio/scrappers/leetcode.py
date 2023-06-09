import os
import requests
from bs4 import BeautifulSoup



def scrap():
    url = f"https://leetcode.com/mukeremali112/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")
    rank_element = soup.find("span", class_="ttext-label-1 dark:text-dark-label-1 font-medium")

    score = score_element.text.strip() if score_element else "N/A"
    rank = rank_element.text.strip() if rank_element else "N/A"

    absolute_logo_url = "../../media/scrape/halloffame.png"

    name = "Leetcode"
    return name, absolute_logo_url,score, rank

# Usage
