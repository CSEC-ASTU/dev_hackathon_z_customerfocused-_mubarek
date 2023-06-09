import requests
from bs4 import BeautifulSoup

def get_kattis_stats():
    url = f"https://open.kattis.com/users/mukerem"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all("span", class_="important_number")[1]
    rank_element = soup.find_all("span", class_="important_number")[0]

    score = score_element.text.strip() if score_element else "N/A"
    rank = rank_element.text.strip() if rank_element else "N/A"

    return score, rank

# Usage
score, rank = get_kattis_stats()
print(f"Solved: {score}")
print(f"Rank from All: {rank}")
