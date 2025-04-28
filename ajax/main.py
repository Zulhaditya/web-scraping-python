import requests
from bs4 import BeautifulSoup

# 1. buka browser lalu mode inspect
# 2. ke tab network dan pilih fetch XHR
# 3. ambil url nya yang akan nge-load data

BASE_URL = "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015"
response = requests.get(BASE_URL)
items = response.json()

result = []
for item in items:
    title = item.get("title")
    year = item.get("year")
    awards = item.get("awards")

    result.append(
        {
            "title": title,
            "year": year,
            "awards": awards,
        }
    )

for item in result:
    print(f"Title: {item['title']} - Year: {item['year']} - Awards: {item['awards']}")
