import requests
from bs4 import BeautifulSoup

# 1. buka browser dan inpsect halaman target
# 2. ke tab network lalu centang all lalu reload websitenya
# 3. cari url yang relevan dan temukan User-Agent
# 4. buat object baru dari User-Agent tersebut

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

response = requests.get(
    "https://www.scrapethissite.com/pages/advanced/?gotcha=headers", headers=headers
)

if response.status_code == 200:
    print("Berhasil request ke website target!")
else:
    print("Gagal request ke website target dengan status code:", response.status_code)

print(response.text)
