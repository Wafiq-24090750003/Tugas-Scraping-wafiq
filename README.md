# CNN Indonesia News Scraping

## Deskripsi Proyek
Proyek ini merupakan tugas web scraping menggunakan Python untuk mengumpulkan data berita dari CNN Indonesia melalui RSS feed. Data yang diperoleh diolah dan disimpan dalam format CSV agar dapat digunakan untuk analisis data.

## Tujuan
- Mempelajari proses web scraping menggunakan Python.
- Mengumpulkan informasi berita dari sumber resmi.
- Mengolah data menggunakan Pandas.
- Menyimpan hasil scraping ke dalam file CSV.

## Sumber Data
- Website: https://www.cnnindonesia.com/
- RSS Feed: https://www.cnnindonesia.com/rss

## Teknologi yang Digunakan
- Python
- Requests
- Pandas
- XML ElementTree

## Proses Scraping
1. Mengakses RSS feed CNN Indonesia menggunakan Requests.
2. Membaca respons dalam format XML.
3. Mengambil judul, tanggal publikasi, URL berita, dan ringkasan jika tersedia.
4. Mengolah data menjadi DataFrame menggunakan Pandas.
5. Menyimpan hasil ke file `cnnindonesia.csv`.

## Data yang Dikumpulkan
File `cnnindonesia.csv` berisi kolom:
- `judul`: judul berita.
- `tanggal`: tanggal publikasi.
- `url`: tautan berita.
- `ringkasan`: ringkasan berita jika tersedia.

## Struktur Proyek
```text
Tugas-Scraping-wafiq/
├── Scraping.py
├── cnnindonesia.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## Cara Menjalankan
Pastikan Python sudah terpasang dan dependensi tersedia.

Instal dependensi:
```bash
pip install -r requirements.txt
```

Jalankan program:
```bash
python Scraping.py
```

Hasil scraping akan disimpan ke `cnnindonesia.csv`.

## Catatan
Jumlah berita yang diperoleh bergantung pada data yang tersedia di RSS feed saat program dijalankan. Pengambilan data harus mengikuti ketentuan penggunaan sumber.

## Penulis
Wafiq Nur Azizah
