import requests
from bs4 import BeautifulSoup

def get_cses_stats():
    url = f"https://cses.fi/user/119282"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all("td")[1]

    score = score_element.text.strip() if score_element else "N/A"
    rank = ''
    return score, rank

# Usage
score, rank = get_cses_stats()
print(f"Submission Count: {score}")
