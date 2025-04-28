import csv
import requests
from bs4 import BeautifulSoup

# ambil request dari website target
response = requests.get("https://www.scrapethissite.com/pages/forms/")
# print(response.status_code)

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
page_num = 1
result = []

while True:
    url = f"{BASE_URL}?page_num={page_num}&per_page=100"
    print(f"Fetching page {url}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Gagal load data page {page_num}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="table")
    rows = table.find_all("tr", class_="team")

    if not rows:
        print(f"Tidak ada data yang bisa ditemukan lagi {page_num}")
        break

    for row in rows:
        team_name = row.find("td", class_="name").get_text(strip=True)
        year = row.find("td", class_="year").get_text(strip=True)
        wins = row.find("td", class_="wins").get_text(strip=True)
        losses = row.find("td", class_="losses").get_text(strip=True)

        result.append(
            {"team_name": team_name, "year": year, "wins": wins, "losses": losses}
        )

    page_num += 1

for item in result:
    # print(
    #     f"Nama Tim: {item['team_name']} - Tahun: {item['year']} - Menang: {item['wins']} - Kalah: {item['losses']}"
    # )

    # export ke football.csv
    with open("football.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldNames = ["team_name", "year", "wins", "losses"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        writer.writeheader()
        for item in result:
            writer.writerow(item)
