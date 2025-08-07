**Judul Proyek:**
Analisis Strategis Umpan Balik E-Commerce Menggunakan IBM Granite untuk Meningkatkan Strategi Produk dan Retensi Pelanggan

**Tinjauan Proyek (Project Overview)**
Proyek ini bertujuan untuk menggunakan AI IBM Granite untuk menganalisis ulasan pelanggan yang tidak terstruktur dan mengubahnya menjadi wawasan bisnis yang strategis. Ini dilakukan melalui klasifikasi topik, analisis sentimen, dan peringkasan otomatis untuk memahami isu-isu utama pelanggan. Tujuannya adalah untuk meningkatkan strategi produk, memperkuat retensi pelanggan, dan memberikan keunggulan kompetitif bagi perusahaan.

**Latar Belakang**
Persaingan ketat di industri ritel modern menuntut perusahaan untuk menjadi sangat responsif terhadap suara pelanggan (voice of customer). PT. Ritel Cemerlang mengumpulkan data masif berupa lebih dari 15.000 ulasan produk setiap bulan, namun gagal mengubahnya menjadi keunggulan kompetitif. Akar masalahnya terletak pada proses analisis manual yang tidak lagi memadai untuk volume dan kompleksitas data saat ini.

Metode manual ini secara langsung menyebabkan kerugian bisnis. Keputusan produk yang tidak berbasis data spesifik dan manajemen inventaris yang reaktif menyebabkan penumpukan stok tidak laku (dead stock). Di sisi lain, strategi pemasaran kehilangan relevansi karena tidak menyoroti fitur yang benar-benar dihargai pelanggan, sementara kegagalan mengatasi keluhan tersembunyi berdampak pada penurunan tingkat retensi. Kondisi ini menciptakan kebutuhan mendesak bagi perusahaan untuk berinvestasi dalam teknologi analisis data canggih, seperti Natural Language Processing (NLP), untuk menggali wawasan yang akurat dan dapat ditindaklanjuti dari ulasan pelanggan.

**Permasalahan (Problem Statement)**
&nbsp;	Berdasarkan dokumen yang diunggah, kesimpulan permasalahannya adalah \*\*perusahaan ritel tidak mampu mengubah volume besar ulasan pelanggan menjadi wawasan bisnis yang strategis karena masih menggunakan metode analisis manual yang tidak efisien\*\*.
Hal ini secara langsung menyebabkan kerugian dan kehilangan peluang di berbagai area bisnis inti:
    * Pengembangan Produk menjadi tidak terarah:\*\* Keputusan penting dibuat berdasarkan intuisi, bukan data spesifik mengenai fitur apa yang benar-benar disukai atau tidak disukai oleh pelanggan.
    * Manajemen Inventaris menjadi reaktif:\*\* Perusahaan gagal mengidentifikasi produk bermasalah secara proaktif, yang mengakibatkan penumpukan stok barang yang tidak laku.
    * Pemasaran menjadi tidak efektif:\*\* Pesan pemasaran bersifat umum dan kehilangan kesempatan untuk menyoroti keunggulan produk yang paling dihargai oleh pelanggan.
    * Retensi Pelanggan menurun:\*\* Masalah spesifik pelanggan tidak teratasi dengan cepat, sehingga loyalitas berkurang dan pelanggan berpotensi beralih ke kompetitor.

Intinya, masalah utamanya adalah adanya kesenjangan kritis antara data umpan balik pelanggan yang melimpah dengan kemampuan perusahaan untuk memanfaatkannya secara efektif untuk pengambilan keputusan yang cerdas dan berbasis data.

**Tujuan (Goals)**
Tujuan utamanya adalah merancang, membangun, dan memvalidasi sebuah kerangka kerja analitis berbasis AI menggunakan IBM Granite untuk mengubah ulasan pelanggan yang tidak terstruktur menjadi wawasan bisnis yang dapat ditindaklanjuti.

Goals bisnis yang diharapkan dari proyek ini meliputi:

    * Meningkatkan kesesuaian produk dengan pasar (product-market fit).
    * Mengurangi tingkat pengembalian produk.
    * Meningkatkan efektivitas kampanye pemasaran.
    * Memperkuat retensi pelanggan.

Secara keseluruhan, tujuan jangka panjangnya adalah meningkatkan profitabilitas dan keunggulan kompetitif perusahaan.

**Tautan dan Deskripsi Dataset (Raw Dataset Link)**
Dataset yang digunakan dalam analisis ini bersumber dari Kaggle. Data ini mencakup informasi mengenai ulasan teks pelanggan, rating produk, status rekomendasi, usia pelanggan, dan detail kategori produk seperti nama divisi, departemen, dan kelas.

**Tautan Dataset Mentah**
`https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews`

**Deskripsi Data**
Dataset ini terdiri dari 23486 baris dan 10 kolom. Kolom-kolom utamanya meliputi:

    * Clothing ID: ID unik untuk setiap item pakaian yang diulas.
    * Age: Usia pelanggan yang memberikan ulasan.
    * Title: Judul dari ulasan.
    * Review Text: Isi teks dari ulasan yang diberikan pelanggan.
    * Rating: Peringkat numerik yang diberikan oleh pelanggan dengan skala 1 (terburuk) hingga 5 (terbaik).
    * Recommended IND: Variabel biner yang menyatakan apakah pelanggan merekomendasikan produk (1 untuk direkomendasikan, 0 untuk tidak).
    * Positive Feedback Count: Jumlah pelanggan lain yang menganggap ulasan tersebut bermanfaat atau positif.
    * Division Name: Nama kategori umum (divisi) dari produk.
    * Department Name: Nama departemen dari produk.
    * Class Name: Nama kategori spesifik (kelas) dari produk.

**Wawasan \& Temuan (Insight \& Findings)**
Berikut adalah temuan utama dari analisis ini:
    * ***Temuan 1: Peringkat Bintang Saja Tidak Cukup untuk Memahami Sentimen Pelanggan***, Analisis menunjukkan bahwa banyak ulasan dengan rating tinggi (misalnya bintang 4) sebenarnya menyembunyikan keluhan spesifik yang signifikan, terutama terkait masalah "Ukuran \& Kesesuaian". Hal ini membuktikan bahwa hanya mengandalkan peringkat bintang dapat menutupi masalah krusial dan menyebabkan perusahaan kehilangan peluang untuk meningkatkan kepuasan pelanggan yang sebenarnya hampir tercapai.
    * ***Temuan 2: Adanya Kesenjangan Persepsi Antar Kelompok Usia***, Ditemukan bahwa pelanggan yang lebih muda (20-30 tahun) cenderung lebih memprioritaskan "Gaya \& Penampilan", sementara pelanggan yang lebih tua (46+ tahun) jauh lebih sensitif terhadap "Kualitas \& Rasa Kain" dan "Ukuran \& Kesesuaian". Umpan balik dari kelompok usia yang lebih tua ini berfungsi sebagai "penanda kualitas" yang penting, dan mengabaikannya dapat berisiko mengasingkan segmen pelanggan yang loyal dan bernilai tinggi.
    * ***Temuan 3: Terungkapnya "Permata Tersembunyi" dan "Pembunuh Senyap" dalam Portofolio Produk***, Analisis data berhasil mengidentifikasi dua kategori produk yang kontradiktif:
        1. "Permata Tersembunyi": Produk dengan rating rata-rata sedang namun tingkat rekomendasinya sangat tinggi, biasanya karena memiliki satu fitur yang sangat disukai pelanggan.
        2. "Pembunuh Senyap": Produk dengan rating tinggi namun tingkat rekomendasinya rendah, yang mengindikasikan adanya masalah fundamental berulang (contoh: menyusut setelah dicuci).
        3. Temuan ini memberikan wawasan langsung untuk strategi pemasaran dan manajemen inventaris.
        4. Penjelasan Dukungan AI (AI Support Explanation)
        5. Proyek ini memanfaatkan teknologi AI untuk melakukan analisis yang mendalam dan efisien. Transparansi dalam penggunaan AI sangat penting untuk kredibilitas proyek.    

**Alat yang Digunakan**

Model AI Utama:
* IBM Granite 3.3 8B Instruct: Model Bahasa Besar (LLM) yang menjadi inti analisis untuk melakukan klasifikasi topik, analisis sentimen, dan peringkasan ulasan pelanggan secara cerdas.

Platform dan Kerangka Kerja AI:
* Replicate: Platform yang digunakan sebagai host untuk menjalankan model IBM Granite melalui API.
* LangChain (khususnya `langchain\_community`): Kerangka kerja (framework) yang mempermudah interaksi dan integrasi dengan model LLM seperti Granite.

Library Analisis \& Visualisasi Data (Python):
* Pandas: Digunakan untuk memuat, membersihkan, dan memanipulasi data ulasan dalam format DataFrame.
* Seaborn \& Matplotlib: Digunakan untuk membuat berbagai visualisasi data, seperti grafik batang (distribusi rating, departemen), histogram (distribusi usia), dan heatmap.
* WordCloud: Digunakan untuk membuat visualisasi **word cloud** yang menyoroti kata-kata kunci dalam ulasan positif dan negatif.
* NLTK (Natural Language Toolkit): Digunakan untuk pra-pemrosesan teks dasar seperti tokenisasi dan penghapusan \*stopwords\* (kata-kata umum).

Library Statistik (Python):
* sciPy: Digunakan untuk melakukan uji statistik Chi-Square guna memeriksa signifikansi hubungan antara variabel kategori (misalnya, antara Departemen dan Rekomendasi).

Lingkungan \& Bahasa:
* Python: Bahasa pemrograman yang digunakan untuk semua analisis dan pemodelan.
* Google Colab: Lingkungan kerja interaktif tempat kode, visualisasi, dan narasi analisis digabungkan (berdasarkan format file `.ipynb`).

**Kesimpulan \& Rekomendasi (Conclusion \& Recommendation)**
1. &nbsp;Peringkat Bintang Tidak Cukup untuk Mengukur Kepuasan
Kesimpulan: Analisis membuktikan bahwa peringkat bintang saja bisa menyesatkan. Banyak ulasan dengan rating tinggi (bintang 4) ternyata menyembunyikan keluhan spesifik yang signifikan, terutama terkait masalah "Ukuran \& Kesesuaian".

Rekomendasi: Untuk Tim Operasi E-Commerce: Rombak total panduan ukuran (sizing charts), khususnya untuk departemen "Dresses" dan "Pants", dengan mengintegrasikan umpan balik langsung dari pelanggan untuk mengurangi tingkat pengembalian produk.

Untuk Tim Produk \& Jaminan Kualitas: Jangan hanya mengandalkan rating tinggi. Segera selidiki produk "Pembunuh Senyap" (rating tinggi, rekomendasi rendah) untuk menemukan masalah fundamental yang berulang.

2. Terdapat Kesenjangan Persepsi Antar Kelompok Usia
Kesimpulan: Pelanggan yang lebih muda (20-30 tahun) lebih memprioritaskan "Gaya \& Penampilan", sementara pelanggan yang lebih tua (46+ tahun) sangat sensitif terhadap "Kualitas \& Rasa Kain". Umpan balik dari kelompok usia yang lebih tua ini berfungsi sebagai "penanda kualitas" yang kritis.

Rekomendasi: Untuk Tim Pemasaran: Buat kampanye iklan yang tersegmentasi untuk menargetkan kelompok usia yang berbeda dengan pesan yang relevan (misalnya, iklan berfokus pada gaya untuk audiens muda, dan iklan berfokus pada kualitas untuk audiens yang lebih tua).

Untuk Tim Produk \& Jaminan Kualitas: Implementasikan sistem "Peringatan Dini Kualitas" yang secara otomatis memicu tinjauan produk jika ada peningkatan keluhan terkait kualitas dari demografi usia 46+.

3\. Portofolio Produk Memiliki Anomali Tersembunyi
Kesimpulan: Analisis data berhasil mengidentifikasi "Permata Tersembunyi" (rating sedang, rekomendasi tinggi) yang potensinya belum dimanfaatkan, dan "Pembunuh Senyap" (rating tinggi, rekomendasi rendah) yang merusak reputasi secara diam-diam.

Rekomendasi: Untuk Tim Pemasaran \& Merchandising: Revisi deskripsi produk untuk "Permata Tersembunyi" dengan menggunakan tema dari ringkasan ulasan positif yang dihasilkan AI untuk menonjolkan fitur yang paling disukai pelanggan.

Untuk Tim Produk \& Jaminan Kualitas: Lakukan analisis akar masalah pada produk "Pembunuh Senyap" untuk segera menemukan dan memperbaiki penyebab utama keluhan pelanggan atau mempertimbangkan untuk menghapusnya dari daftar produk.

**AI SUPPORT EXPLANATION**
Analisis Umpan Balik Pelanggan Menggunakan AI
Proyek ini memanfaatkan kekuatan Kecerdasan Buatan untuk menganalisis dan mengekstrak wawasan berharga dari ulasan pelanggan.

Peran Kecerdasan Buatan dalam Analisis Ini
Analisis mendalam terhadap umpan balik pelanggan yang disajikan dalam studi kasus ini dimungkinkan secara signifikan berkat pemanfaatan Model Bahasa Besar (LLM), khususnya IBM Granite. Alat AI ini bukan sekadar pengganti otomatisasi sederhana, melainkan agen cerdas yang mampu memahami, menginterpretasikan, dan mengekstraksi makna dari teks yang tidak terstruktur dengan cara yang sebelumnya sulit atau memakan biaya besar untuk dilakukan.

    *   IBM Granite: Kekuatan di Balik Wawasan
    Model IBM Granite 3.3 8B Instruct mengubah ulasan pelanggan yang tidak terstruktur menjadi data bisnis yang dapat ditindaklanjuti berkat kemampuan intinya:
    *   Pemahaman Konteks: Mampu memahami nuansa dan sarkasme dalam ulasan, tidak hanya terpaku pada kata kunci.
    *   Klasifikasi Spesifik: Dapat dilatih untuk mengkategorikan umpan balik ke dalam topik bisnis yang terperinci seperti "Ukuran & Kesesuaian".
    *   Peringkasan Efektif: Unggul dalam meringkas volume besar ulasan menjadi poin-poin penting yang ringkas dan relevan.
    *   Skalabilitas: Arsitekturnya mampu menangani analisis data dalam skala besar, dari ribuan hingga jutaan ulasan.

Secara keseluruhan, model ini memungkinkan perusahaan untuk dengan cepat mengubah data kualitatif menjadi intelijen bisnis untuk strategi produk dan pengalaman pelanggan yang lebih baik.


