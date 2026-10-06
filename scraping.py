import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kopikenangan.com"

response = requests.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(
    "Judul website:",
    soup.title.text if soup.title else "Tidak ditemukan"
)

data = {
    "nama": ["Kopi Kenangan"],
    "website": [url],
    "judul": [soup.title.text if soup.title else "Tidak ditemukan"]
}

df = pd.DataFrame(data)
df.to_csv("kopi_kenangan.csv", index=False)

print("Data berhasil disimpan ke kopi_kenangan.csv")