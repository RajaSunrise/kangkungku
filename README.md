# KangkungKu - Sistem Pakar Diagnosa Penyakit Kangkung

Aplikasi Sistem Pakar untuk mendiagnosa penyakit pada tanaman Kangkung Air menggunakan metode **Certainty Factor (CF)**. Aplikasi ini dibangun dengan **FastAPI** (Python) dan antarmuka web modern menggunakan HTML & Tailwind CSS.

## 1. Diagram Alir Sistem (Flowchart)

Berikut adalah alur proses diagnosa dalam sistem:

```mermaid
flowchart TD
    A([Mulai]) --> B[Pengguna Memilih Gejala yang Diamati]
    B --> C[Pengguna Memasukkan Tingkat Keyakinan (CF User)]
    C --> D{Apakah ada gejala lain?}
    D -- Ya --> B
    D -- Tidak --> E[Sistem Mengambil Data Aturan & Bobot Pakar]
    E --> F[Hitung CF Pakar * CF User]
    F --> G[Hitung CF Kombinasi untuk Setiap Penyakit]
    G --> H[Urutkan Hasil Diagnosa Berdasarkan Nilai CF Tertinggi]
    H --> I[Tampilkan Hasil Diagnosa & Solusi]
    I --> J([Selesai])
```

## 2. Use Case Diagram

Diagram interaksi pengguna dengan sistem:

```mermaid
usecaseDiagram
    actor Pengguna
    package "Sistem Pakar KangkungKu" {
        usecase "Melihat Daftar Gejala" as UC1
        usecase "Melakukan Diagnosa" as UC2
        usecase "Melihat Hasil & Solusi" as UC3
        usecase "Melihat Daftar Penyakit" as UC4
    }
    Pengguna --> UC1
    Pengguna --> UC2
    Pengguna --> UC3
    Pengguna --> UC4
    UC2 ..> UC1 : include
    UC3 ..> UC2 : include
```

## 3. Entity Relationship Diagram (ERD)

Struktur basis data yang digunakan:

```mermaid
erDiagram
    PENYAKIT ||--|{ ATURAN : memiliki
    GEJALA ||--|{ ATURAN : memiliki

    PENYAKIT {
        int id PK
        string nama
        string nama_ilmiah
        text deskripsi
        text solusi
        string url_gambar
    }

    GEJALA {
        int id PK
        string kode
        string deskripsi
        string url_gambar
    }

    ATURAN {
        int id PK
        int penyakit_id FK
        int gejala_id FK
        float pakar_cf "Bobot Pakar (0-1)"
    }
```

## 4. Tabel Data Penyakit

Daftar 15 penyakit yang dapat didiagnosa oleh sistem:

| No | Nama Penyakit | Nama Ilmiah |
|---|---|---|
| 1 | Karat Putih (White Rust) | *Albugo ipomoeae-panduratae* |
| 2 | Bercak Daun Cercospora | *Cercospora ipomoeae* |
| 3 | Virus Mosaik Kangkung | *Water spinach mosaic virus* |
| 4 | Layu Fusarium | *Fusarium oxysporum* |
| 5 | Busuk Akar Pythium | *Pythium spp.* |
| 6 | Busuk Batang Rhizoctonia | *Rhizoctonia solani* |
| 7 | Bercak Daun Alternaria | *Alternaria spp.* |
| 8 | Bercak Daun Bakteri | *Pseudomonas / Xanthomonas* |
| 9 | Embun Tepung (Powdery Mildew) | *Erysiphe spp.* |
| 10 | Embun Bulu (Downy Mildew) | *Peronospora spp.* |
| 11 | Antraknosa | *Colletotrichum spp.* |
| 12 | Serangan Kutu Daun (Aphids) | *Aphidoidea* |
| 13 | Serangan Tungau Laba-laba | *Tetranychidae* |
| 14 | Pengorok Daun (Leaf Miner) | *Liriomyza spp.* |
| 15 | Kekurangan Nitrogen | *Nutrient Deficiency* |

## 5. Tabel Data Gejala

Daftar 25 gejala yang digunakan untuk diagnosa:

| Kode | Deskripsi Gejala |
|---|---|
| G01 | Bercak putih menonjol pada sisi bawah daun |
| G02 | Bercak kuning pada sisi atas daun |
| G03 | Daun melengkung atau terdistorsi |
| G04 | Bercak bulat dengan pusat abu-abu/putih |
| G05 | Bercak dengan tepi coklat tua/merah |
| G06 | Pola mosaik hijau terang/gelap pada daun |
| G07 | Pertumbuhan tanaman kerdil |
| G08 | Daun bagian bawah menguning |
| G09 | Tanaman layu pada siang hari, pulih malam hari |
| G10 | Jaringan pembuluh batang berwarna coklat |
| G11 | Akar berwarna coklat dan lembek |
| G12 | Batang lunak dan gelap di dekat tanah |
| G13 | Lesi cekung kemerahan pada batang |
| G14 | Bercak seperti target dengan cincin konsentris |
| G15 | Bercak basah dikelilingi halo kuning |
| G16 | Serbuk putih pada permukaan daun |
| G17 | Pertumbuhan berbulu halus abu-abu/ungu di bawah daun |
| G18 | Lesi cekung gelap pada batang/daun |
| G19 | Serangga kecil berkumpul di pucuk/bawah daun |
| G20 | Bintik-bintik kuning/putih halus pada daun |
| G21 | Jaring halus pada tanaman |
| G22 | Terowongan putih berkelok-kelok di dalam daun |
| G23 | Daun tua menguning secara menyeluruh |
| G24 | Daun berlubang (shot-holes) |
| G25 | Massa spora merah muda terlihat |

## 6. Tabel Basis Pengetahuan (Rule dan Bobot Pakar)

Contoh aturan dan nilai CF (Certainty Factor) dari pakar:

| Nama Penyakit | Kode Gejala | CF Pakar |
|---|---|---|
| Karat Putih | G01 | 0.9 |
| Karat Putih | G02 | 0.7 |
| Karat Putih | G03 | 0.5 |
| Bercak Daun Cercospora | G04 | 0.8 |
| Bercak Daun Cercospora | G05 | 0.8 |
| Bercak Daun Cercospora | G08 | 0.4 |
| Virus Mosaik Kangkung | G06 | 0.95 |
| Virus Mosaik Kangkung | G03 | 0.6 |
| Virus Mosaik Kangkung | G07 | 0.7 |
| Layu Fusarium | G08 | 0.6 |
| Layu Fusarium | G09 | 0.9 |
| ... | ... | ... |

*(Tabel lengkap mencakup seluruh relasi di database)*

## 7. Tabel Konversi Bobot Pengguna (User)

Pengguna dapat memasukkan tingkat keyakinan terhadap gejala yang dialami menggunakan slider (0.1 - 1.0). Berikut interpretasi nilainya:

| Nilai CF User | Tingkat Keyakinan |
|---|---|
| 0.0 - 0.2 | Tidak Tahu / Sangat Ragu |
| 0.2 - 0.4 | Sedikit Yakin |
| 0.4 - 0.6 | Cukup Yakin |
| 0.6 - 0.8 | Yakin |
| 0.8 - 1.0 | Sangat Yakin |

## 8. Simulasi Perhitungan Certainty Factor Secara Manual

Misalkan pengguna memilih gejala untuk penyakit **Karat Putih** dengan keyakinan tertentu:

1.  **Gejala 1 (G01)**: Bercak putih menonjol
    *   CF Pakar: 0.9
    *   CF User: 0.8 (Sangat Yakin)
    *   **CF(1)** = 0.9 * 0.8 = **0.72**

2.  **Gejala 2 (G02)**: Bercak kuning
    *   CF Pakar: 0.7
    *   CF User: 0.6 (Cukup Yakin)
    *   **CF(2)** = 0.7 * 0.6 = **0.42**

3.  **Perhitungan CF Kombinasi (CF Combine)**:
    Rumus: $CF_{new} = CF_{old} + CF_{current} \times (1 - CF_{old})$

    *   Langkah 1 (Gabungkan CF1 dan CF2):
        $$CF_{old} = CF(1) = 0.72$$
        $$CF_{current} = CF(2) = 0.42$$
        $$CF_{combine} = 0.72 + 0.42 \times (1 - 0.72)$$
        $$CF_{combine} = 0.72 + 0.42 \times 0.28$$
        $$CF_{combine} = 0.72 + 0.1176$$
        $$CF_{combine} = \mathbf{0.8376}$$

    *   **Hasil Akhir**: Tingkat keyakinan sistem untuk penyakit Karat Putih adalah **83.76%**.

## 9. Alur Antarmuka Pengguna (User Interface)

1.  **Halaman Utama (Home)**: Pengenalan sistem dan tombol mulai diagnosa.
2.  **Halaman Diagnosa**:
    *   Daftar gejala ditampilkan dalam bentuk kartu grid.
    *   Pengguna mengklik gejala yang dialami.
    *   Slider muncul untuk mengatur tingkat keyakinan (default 0.8).
    *   Tombol "Dapatkan Hasil" memproses data ke server.
3.  **Halaman Hasil**:
    *   Menampilkan penyakit dengan persentase tertinggi.
    *   Detail penyakit (Deskripsi, Nama Ilmiah, Gambar).
    *   Solusi penanganan yang disarankan.
    *   Tabel rincian perhitungan gejala yang dipilih.

## 10. Pengujian Akurasi Sistem (Validasi Pakar)

Akurasi sistem divalidasi dengan membandingkan hasil diagnosa sistem dengan diagnosa pakar asli terhadap sejumlah kasus uji.

Metode pengujian:
1.  **Confusion Matrix**: Menghitung True Positive, False Positive, True Negative, dan False Negative.
2.  **Tingkat Akurasi**: $\frac{\text{Jumlah Kasus Benar}}{\text{Total Kasus}} \times 100\%$

Sistem ini dirancang untuk memberikan rekomendasi awal. Jika hasil diagnosa memiliki persentase rendah (< 50%), disarankan untuk berkonsultasi langsung dengan ahli pertanian.
