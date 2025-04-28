import requests
from bs4 import BeautifulSoup
import csv

# ambil request dari website target
response = requests.get("https://www.scrapethissite.com/pages/simple/")
print(response.status_code)
# print(response.text)

# ekstrak response dari html ke bentuk text
soup = BeautifulSoup(response.text, "html.parser")
country_blocks = soup.find_all("div", class_="col-md-4 country")
print(f"Jumlah negara yang ada di website: {len(country_blocks)}")

result = []
for block in country_blocks:
    # cari seluruh h3 pada class country-name dan dapatkan nama dari setiap negara
    name_element = block.find("h3", class_="country-name")
    country_name = name_element.get_text(strip=True)

    # cari seluruh span pada class country-capital dan dapatkan nama capital dari setiap negara
    capital_element = block.find("span", class_="country-capital")
    capital_name = capital_element.get_text(strip=True)

    # cari seluruh span pada class country-population dan dapatkan jumlah populasi dari setiap negara
    population_element = block.find("span", class_="country-population")
    count_population = population_element.get_text(strip=True)

    # cari seluruh span pada class country-area dan dapatkan total luas area dari setiap negara
    area_element = block.find("span", class_="country-area")
    count_area = area_element.get_text(strip=True)

    result.append(
        {
            "name": country_name,
            "capital": capital_name,
            "population": count_population,
            "area": count_area,
        }
    )

for item in result:
    print(
        f"Negara: {item['name']} - Ibukota: {item['capital']} - Jumlah Populasi: {item['population']} - Luas: {item['area']}"
    )

    # eksport ke countries.csv
    with open("countries.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldNames = ["name", "capital", "population", "area"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        writer.writeheader()
        for item in result:
            writer.writerow(item)
