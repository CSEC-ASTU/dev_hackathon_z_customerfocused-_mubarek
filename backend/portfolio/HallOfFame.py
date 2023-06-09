import requests
from bs4 import BeautifulSoup

def scrape_halloffame_points():
    url = f"https://cphof.org/profile/codeforces:mukeremali"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    points_element = soup.find_all("td", class_="light-cell")[-1]
    points_elements = soup.find_all("td", class_="light-cell")[0]
    points = points_element.text.strip() if points_element else "N/A"
    point = points_elements.text.strip() if points_elements else "N/A"

    return points, point

# Usage
points, point = scrape_halloffame_points()
print(f"Rank: {points}")
print(f"Title: {point}")
