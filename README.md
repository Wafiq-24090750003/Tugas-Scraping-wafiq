# CNN Indonesia News Scraping

## Deskripsi Proyek
Proyek ini dibuat untuk mengambil data berita dari CNN Indonesia menggunakan Python. Data berita dikumpulkan melalui RSS feed, kemudian diolah dan disimpan dalam format CSV agar lebih mudah dibaca dan dianalisis.

## Tujuan
- Mempelajari proses web scraping menggunakan Python.
- Mengumpulkan informasi berita dari sumber daring.
- Mengolah data menggunakan Pandas.
- Menyimpan hasil pengumpulan data ke dalam file CSV.

## Sumber Data
- Website: [CNN Indonesia](https://www.cnnindonesia.com/)
- RSS Feed: [CNN Indonesia RSS](https://www.cnnindonesia.com/rss)

## Teknologi yang Digunakan
- Python
- Requests
- Pandas
- XML ElementTree

## Data yang Dikumpulkan
File `cnnindonesia.csv` berisi kolom:
- `judul`: judul berita.
- `tanggal`: tanggal publikasi berita.
- `url`: tautan menuju artikel.
- `ringkasan`: ringkasan berita jika tersedia pada RSS feed.

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
1. Pastikan Python sudah terpasang.
2. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan program:
   ```bash
   python Scraping.py
   ```
4. Hasil pengumpulan data akan disimpan ke `cnnindonesia.csv`.

## Catatan
Jumlah dan isi berita bergantung pada data yang tersedia di RSS feed saat program dijalankan. Gunakan data sesuai ketentuan dan kebijakan sumbernya.

## Penulis
Wafiq Nur Azizah