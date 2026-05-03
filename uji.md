# Tabel Pengujian Sistem KangkungKu (Black Box Testing)

**Tabel 4.26 Detail Pengujian Fungsionalitas Sistem**

| No | Kasus/Diuji | Skenario Uji | Hasil Yang Diharapkan | Hasil Pengujian |
|:---|:---|:---|:---|:---|
| **A** | **AUTENTIKASI & AKSES** | | | |
| 1 | Login Admin/User | Memasukkan username dan password yang valid | Sistem mengalihkan ke dashboard sesuai role | [√] Berhasil <br> [ ] Tidak Berhasil |
| 2 | Login Gagal | Memasukkan password yang salah | Sistem menampilkan pesan "Username atau password salah" | [√] Berhasil <br> [ ] Tidak Berhasil |
| 3 | Logout | Menekan tombol logout pada menu navigasi | Sesi dihapus dan diarahkan kembali ke login | [√] Berhasil <br> [ ] Tidak Berhasil |
| 4 | Proteksi URL | Mengakses URL admin tanpa login | Sistem memaksa redirect ke halaman login | [√] Berhasil <br> [ ] Tidak Berhasil |
| **B** | **MANAJEMEN PENYAKIT** | | | |
| 5 | Lihat Daftar Penyakit | Mengklik menu "Penyakit" di sidebar | Menampilkan tabel data penyakit secara lengkap | [√] Berhasil <br> [ ] Tidak Berhasil |
| 6 | Tambah Penyakit | Mengisi form tambah (nama, deskripsi, solusi, foto) | Data baru tersimpan dan muncul di tabel | [√] Berhasil <br> [ ] Tidak Berhasil |
| 7 | Validasi Tambah | Menekan simpan tanpa mengisi nama penyakit | Sistem memberikan peringatan input wajib diisi | [√] Berhasil <br> [ ] Tidak Berhasil |
| 8 | Update Penyakit | Mengubah deskripsi penyakit yang sudah ada | Perubahan tersimpan secara permanen di database | [√] Berhasil <br> [ ] Tidak Berhasil |
| 9 | Hapus Penyakit | Menekan ikon hapus dan mengonfirmasi modal | Data terhapus dan hilang dari daftar tabel | [√] Berhasil <br> [ ] Tidak Berhasil |
| **C** | **MANAJEMEN GEJALA** | | | |
| 10 | Lihat Daftar Gejala | Mengklik menu "Gejala" di sidebar | Menampilkan daftar kode dan deskripsi gejala | [√] Berhasil <br> [ ] Tidak Berhasil |
| 11 | Tambah Gejala | Menginput kode (mis: G08) dan deskripsi gejala | Kode gejala baru berhasil didaftarkan | [√] Berhasil <br> [ ] Tidak Berhasil |
| 12 | Update Gejala | Memperbaiki typo pada deskripsi gejala | Deskripsi terbaru tersimpan dengan sukses | [√] Berhasil <br> [ ] Tidak Berhasil |
| 13 | Hapus Gejala | Menghapus gejala yang sudah tidak digunakan | Data gejala berhasil dihapus dari sistem | [√] Berhasil <br> [ ] Tidak Berhasil |
| **D** | **MANAJEMEN ATURAN (BASIS PENGETAHUAN)** | | | |
| 14 | Lihat Aturan | Mengklik menu "Aturan" di sidebar | Menampilkan relasi penyakit, gejala, dan CF Pakar | [√] Berhasil <br> [ ] Tidak Berhasil |
| 15 | Tambah Aturan | Memilih penyakit, gejala, dan mengisi nilai CF | Relasi pakar baru berhasil ditambahkan | [√] Berhasil <br> [ ] Tidak Berhasil |
| 16 | Update Aturan | Mengubah nilai CF Pakar (mis: dari 0.8 ke 0.9) | Nilai CF terbaru diperbarui di sistem | [√] Berhasil <br> [ ] Tidak Berhasil |
| 17 | Hapus Aturan | Menghapus salah satu baris relasi aturan | Aturan tersebut tidak lagi dipakai dalam diagnosa | [√] Berhasil <br> [ ] Tidak Berhasil |
| **E** | **MANAJEMEN PENGGUNA (USERS)** | | | |
| 18 | Lihat Daftar User | Mengklik menu "Pengguna" di sidebar | Menampilkan daftar username, email, dan role | [√] Berhasil <br> [ ] Tidak Berhasil |
| 19 | Tambah User Baru | Admin mendaftarkan user baru secara manual | Akun baru aktif dan bisa digunakan login | [√] Berhasil <br> [ ] Tidak Berhasil |
| 20 | Update Data User | Mengubah status user (Aktif/Non-aktif) atau Role | Status pengguna berubah sesuai pengaturan | [√] Berhasil <br> [ ] Tidak Berhasil |
| 21 | Hapus User | Menghapus akun pengguna tertentu | Data pengguna dihapus permanen dari sistem | [√] Berhasil <br> [ ] Tidak Berhasil |
| **F** | **FITUR DIAGNOSA (CERTAINTY FACTOR)** | | | |
| 22 | Registrasi Mandiri | User baru mengisi form daftar di halaman publik | Akun tersimpan dan user diarahkan ke dashboard | [√] Berhasil <br> [ ] Tidak Berhasil |
| 23 | Input Gejala | Memilih beberapa gejala dan tingkat keyakinan | Pilihan gejala tersimpan sementara untuk diproses | [√] Berhasil <br> [ ] Tidak Berhasil |
| 24 | Proses Hitung CF | Menekan tombol "Proses Diagnosa" | Sistem menghitung CF Pakar * CF User (CF Kombinasi) | [√] Berhasil <br> [ ] Tidak Berhasil |
| 25 | Hasil Diagnosa | Menampilkan hasil akhir diagnosa | Menampilkan penyakit dengan persentase tertinggi | [√] Berhasil <br> [ ] Tidak Berhasil |
| 26 | Solusi Penyakit | Membaca bagian solusi pada hasil diagnosa | Solusi yang ditampilkan sesuai dengan penyakitnya | [√] Berhasil <br> [ ] Tidak Berhasil |
| **G** | **RIWAYAT & INFORMASI** | | | |
| 27 | Lihat Riwayat | User melihat daftar diagnosa sebelumnya | Menampilkan tanggal, penyakit, dan hasil (%) | [√] Berhasil <br> [ ] Tidak Berhasil |
| 28 | Detail Riwayat | Klik detail pada salah satu baris riwayat | Menampilkan kembali halaman hasil diagnosa lama | [√] Berhasil <br> [ ] Tidak Berhasil |
| 29 | Hapus Riwayat | Menghapus riwayat diagnosa tertentu | Baris riwayat hilang dari daftar user | [√] Berhasil <br> [ ] Tidak Berhasil |
| 30 | Ensiklopedia | Membuka daftar penyakit di halaman publik | User bisa membaca informasi penyakit tanpa login | [√] Berhasil <br> [ ] Tidak Berhasil |
| 31 | Pencarian | Mencari data pada tabel (Admin) | Tabel memfilter data secara real-time | [√] Berhasil <br> [ ] Tidak Berhasil |
| 32 | Responsivitas | Mengakses web melalui perangkat mobile | Tampilan menyesuaikan ukuran layar (Responsive) | [√] Berhasil <br> [ ] Tidak Berhasil |
