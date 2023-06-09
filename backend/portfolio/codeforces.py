import requests
from bs4 import BeautifulSoup

def get_codeforce_stats():
    url = f"https://codeforces.com/profile/mukeremali"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find("div", class_="_UserActivityFrame_counterValue")

    score = score_element.text.strip() if score_element else "N/A"
    rank = ''
    return score, rank

# Usage
score, rank = get_codeforce_stats()
print(f"Solved: {score}")
