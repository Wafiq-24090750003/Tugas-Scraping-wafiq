
import requests
from bs4 import BeautifulSoup

url = "https://www.cnnindonesia.com/teknologi"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("Judul halaman:", soup.title.get_text(strip=True))

    links = soup.select("a[href]")

    berita = [
        link for link in links
        if link.get_text(" ", strip=True)
        and "/20" in link.get("href", "")
    ]

    print("Jumlah tautan kandidat berita:", len(berita))

    for link in berita[:100]:
        print(
            link.get_text(" ", strip=True),
            link.get("href")
        )
else:
    print("Halaman yang dapat diakses untuk scraping.")
