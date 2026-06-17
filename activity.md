# Dokumen Alur Aktivitas Sistem (Activity Description) - KangkungKu

Dokumen ini berisi deskripsi tertulis mengenai alur aktivitas sistem (*Activity Description*) untuk seluruh fitur yang ada dalam aplikasi **KangkungKu** (Sistem Pakar Diagnosa Penyakit Kangkung Air). Alur di bawah ini disederhanakan agar mudah dipahami, dengan urutan menggunakan penomoran huruf (a, b, c, dst.) serta membedakan peran antara Admin dan Pengguna.

---

## 1. KELOMPOK AKTIVITAS ADMIN

### 1.1. Login Admin
a. Admin membuka halaman login admin pada aplikasi.
b. Admin memasukkan username dan password.
c. Sistem memverifikasi kredensial data admin ke database.
d. Sistem menampilkan halaman dashboard admin setelah login berhasil.

### 1.2. Kelola (CRUD) Gejala
a. Admin masuk ke halaman tabel daftar data gejala.
b. Admin memilih opsi aksi (tambah, ubah, atau hapus) data gejala.
c. Admin mengisi formulir perubahan data gejala sesuai kebutuhan.
d. Sistem memproses penyimpanan atau perubahan data gejala ke database.
e. Sistem menampilkan notifikasi sukses dan memperbarui tabel data gejala.

### 1.3. Kelola (CRUD) Penyakit
a. Admin masuk ke halaman tabel daftar data penyakit.
b. Admin memilih opsi aksi (tambah, ubah, atau hapus) data penyakit.
c. Admin mengisi formulir informasi penyakit, deskripsi, dan solusi penanganan.
d. Sistem memproses penyimpanan atau perubahan data penyakit ke database.
e. Sistem menampilkan notifikasi sukses dan memperbarui tabel data penyakit.

### 1.4. Kelola (CRUD) Aturan (Rules)
a. Admin masuk ke halaman tabel daftar aturan (rules).
b. Admin memilih opsi aksi (tambah, ubah, atau hapus) relasi aturan.
c. Admin menentukan penyakit, gejala, dan menginput nilai bobot CF Pakar.
d. Sistem memproses penyimpanan atau perubahan data aturan ke database.
e. Sistem menampilkan notifikasi sukses dan memperbarui tabel aturan.

### 1.5. Kelola (CRUD) Pengguna (User)
a. Admin masuk ke halaman tabel daftar akun pengguna (user).
b. Admin memilih opsi aksi (tambah, ubah, atau hapus) data pengguna.
c. Admin mengisi formulir data akun pengguna terdaftar.
d. Sistem memproses penyimpanan atau perubahan data pengguna ke database.
e. Sistem menampilkan notifikasi sukses dan memperbarui tabel data pengguna.

---

## 2. KELOMPOK AKTIVITAS PENGGUNA (USER)

### 2.1. Registrasi Akun Baru
a. Pengguna membuka halaman formulir pendaftaran/registrasi.
b. Pengguna mengisi data pendaftaran berupa username, alamat, dan password.
c. Sistem melakukan validasi dan memeriksa keunikan data ke database.
d. Sistem menyimpan akun pengguna baru ke database.
e. Sistem menampilkan notifikasi registrasi berhasil dan mengarahkan ke halaman login.

### 2.2. Login Pengguna
a. Pengguna membuka halaman login pengguna.
b. Pengguna memasukkan username dan password.
c. Sistem memverifikasi kredensial data pengguna ke database.
d. Sistem mengarahkan pengguna masuk ke halaman utama dashboard pengguna setelah login berhasil.

### 2.3. Proses Diagnosa Penyakit (Certainty Factor)
a. Pengguna masuk ke halaman diagnosis penyakit.
b. Pengguna memilih beberapa gejala yang terlihat pada tanaman kangkung air.
c. Pengguna menginput nilai keyakinan (slider CF User) untuk gejala yang dipilih.
d. Sistem memproses diagnosis menggunakan perhitungan Certainty Factor berdasarkan bobot pakar.
e. Sistem menampilkan hasil penyakit terdiagnosa beserta persentase keyakinan dan solusi penanganannya.

### 2.4. Lihat Riwayat Diagnosa
a. Pengguna memilih menu riwayat diagnosa pada dashboard.
b. Sistem memproses dan mengambil data riwayat diagnosa milik pengguna dari database.
c. Sistem menampilkan daftar tabel riwayat diagnosa yang telah dilakukan.

### 2.5. Lihat Detail Riwayat Diagnosa
a. Pengguna berada pada halaman daftar riwayat diagnosa.
b. Pengguna memilih salah satu riwayat diagnosa untuk melihat rincian detail.
c. Sistem memproses dan mengambil data detail riwayat diagnosa terpilih.
d. Sistem menampilkan rincian gejala yang pernah dipilih beserta perhitungan lengkap dan solusi penyakitnya.

### 2.6. Lihat Ensiklopedia Penyakit
a. Pengguna memilih menu ensiklopedia atau daftar penyakit.
b. Sistem memproses dan mengambil seluruh data informasi penyakit kangkung.
c. Sistem menampilkan halaman daftar penyakit lengkap dengan foto, deskripsi ilmiah, dan cara penanganannya.

### 2.7. Kalkulator Penggunaan Pupuk
a. Pengguna membuka halaman kalkulator pupuk.
b. Pengguna menginput luas lahan atau area sawah tanaman kangkung air (meter persegi).
c. Sistem menghitung rekomendasi takaran pupuk berdasarkan formula standar pertanian.
d. Sistem menampilkan hasil perhitungan rekomendasi jumlah pupuk Urea, TSP, dan KCl.

### 2.8. Logout Pengguna
a. Pengguna menekan tombol logout pada menu navigasi.
b. Sistem menghapus sesi login aktif pengguna pada server.
c. Sistem mengarahkan pengguna kembali ke halaman utama publik (landing page).
