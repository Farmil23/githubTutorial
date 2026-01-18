
# 🐳 GitHub & Docker Tutorial Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)]()

> **Proyek sederhana untuk mendemonstrasikan alur kerja Git, Python, dan kontainerisasi menggunakan Docker.**

Repositori ini dirancang sebagai bahan pembelajaran untuk memahami bagaimana aplikasi Python sederhana dapat dijalankan secara lokal maupun di dalam lingkungan kontainer (Docker). Aplikasi ini membaca data dari file teks dan menjalankannya sebagai layanan.

---

## 👨‍💻 Author

**Nama** : Farhan Kamil Hermansyah  
**NRP** : 152024150  
**Peran** : Developer

---

## 📂 Struktur Proyek

```bash
githubtutorial/
├── data/
│   └── pesan.txt           # File data eksternal yang dibaca aplikasi
├── app.py                  # Script utama aplikasi Python
├── Dockerfile              # Konfigurasi image Docker
├── docker-compose.yml      # Konfigurasi orkestrasi container
├── requirements.txt        # Daftar dependensi Python
└── README.md               # Dokumentasi Proyek

```

---

## 🚀 Cara Menjalankan

Anda dapat menjalankan aplikasi ini dengan dua cara: **Manual (Lokal)** atau menggunakan **Docker**.

### Cara 1: Menjalankan Secara Lokal (Python)

Pastikan Python sudah terinstal di komputer Anda.

1. **Clone Repositori**
```bash
git clone [https://github.com/username-anda/githubTutorial.git](https://github.com/username-anda/githubTutorial.git)
cd githubTutorial

```


2. **Install Dependensi**
```bash
pip install -r requirements.txt

```


3. **Jalankan Aplikasi**
```bash
python app.py

```



### Cara 2: Menjalankan dengan Docker (Disarankan)

Pastikan Docker Desktop sudah berjalan di komputer Anda.

1. **Build & Run dengan Docker Compose**
Cara termudah untuk menjalankan aplikasi adalah dengan satu perintah:
```bash
docker-compose up --build

```


2. **Alternatif: Build Manual**
Jika ingin membangun image secara manual tanpa Docker Compose:
```bash
# Build Image
docker build -t github-tutorial-app .

# Run Container
docker run -p 5000:5000 github-tutorial-app

```



---

## 🛠️ Teknologi yang Digunakan

* **Python**: Bahasa pemrograman utama.
* **Docker**: Untuk mengemas aplikasi agar dapat berjalan di lingkungan apa pun.
* **Docker Compose**: Untuk mendefinisikan dan menjalankan layanan Docker multi-kontainer (jika diperlukan pengembangan lebih lanjut).

---

<div align="center">
<small>Copyright © 2026 Farhan Kamil Hermansyah (152024150)</small>
</div>

```

```
