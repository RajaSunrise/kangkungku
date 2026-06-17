# Entity Relationship Diagram (ERD) - KangkungKu

Berikut adalah struktur basis data aplikasi **KangkungKu** (Sistem Pakar Diagnosa Penyakit Kangkung Air) setelah penghapusan kolom `email` pada tabel `users`.

## 1. Diagram ERD (Mermaid)

```mermaid
erDiagram
    PENYAKIT ||--|{ ATURAN : memiliki
    GEJALA ||--|{ ATURAN : memiliki
    USERS ||--|{ DIAGNOSA_HISTORY : memiliki
    PENYAKIT ||--|{ DIAGNOSA_HISTORY : tercatat_di

    PENYAKIT {
        int id PK
        string nama
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
        float pakar_cf
    }

    USERS {
        int id PK
        string username
        string hashed_password
        string role
        boolean is_active
        text alamat
    }

    DIAGNOSA_HISTORY {
        int id PK
        int user_id FK
        int penyakit_id FK
        float faktor_kepastian
        float persentase
        text gejala_input
        string created_at
    }
```

## 2. Deskripsi Hubungan Antar Tabel
1. **PENYAKIT ke ATURAN (1 to Many)**: Satu penyakit dapat memiliki banyak gejala/aturan yang mengikatnya.
2. **GEJALA ke ATURAN (1 to Many)**: Satu gejala dapat dikaitkan dengan banyak penyakit dalam basis aturan.
3. **USERS ke DIAGNOSA_HISTORY (1 to Many)**: Satu pengguna dapat melakukan dan menyimpan banyak riwayat diagnosa.
4. **PENYAKIT ke DIAGNOSA_HISTORY (1 to Many)**: Satu diagnosa history akan menunjuk pada satu penyakit hasil diagnosa.
