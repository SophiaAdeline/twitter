# twitter

Berikut adalah panduan langkah demi langkah untuk membuat bot Twitter otomatis menggunakan GitHub Actions dan API Gemini:

1. Persiapan Awal

   - Buat Akun Developer Twitter:
     Daftar di https://developer.x.com/en
     Buat project baru dan dapatkan API keys:
       API_KEY
       API_SECRET_KEY
       ACCESS_TOKEN
       ACCESS_TOKEN_SECRET

  - Dapatkan API Key Gemini:
    Kunjungi Google AI Studio https://aistudio.google.com/
    Buat API key untuk Gemini Pro

2. Konfigurasi GitHub Secrets
Tambahkan secrets di repo GitHub (Settings > Secrets):
   TWITTER_API_KEY
   TWITTER_API_SECRET
   TWITTER_ACCESS_TOKEN
   TWITTER_ACCESS_TOKEN_SECRET
   GEMINI_API_KEY

3. Cara Penggunaan
Atur jadwal di config.json menggunakan format cron:
   "0 9 * * *" = Setiap hari jam 09:00 UTC
   "0 14 * * 1" = Setiap Senin jam 14:00 UTC

Ubah parameter lain di config.json:
   link: URL yang ingin dipromosikan
   language: Bahasa konten (contoh: "English", "日本語")
   country_code: Kode negara untuk trending (ID=Indonesia, JP=Jepang)
   max_hashtags: Jumlah maksimal hashtag (1-5)
