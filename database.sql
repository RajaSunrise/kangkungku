-- SQL Script to recreate the KangkungKu database structure and initial data
-- Compatible with MySQL, PostgreSQL, and SQLite

-- 1. Table: penyakit
CREATE TABLE IF NOT EXISTS penyakit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama VARCHAR(35) NOT NULL,
    deskripsi TEXT,
    solusi TEXT,
    url_gambar VARCHAR(255)
);

-- 2. Table: gejala
CREATE TABLE IF NOT EXISTS gejala (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kode VARCHAR(35) UNIQUE NOT NULL,
    deskripsi VARCHAR(35) NOT NULL,
    url_gambar VARCHAR(255)
);

-- 3. Table: aturan
CREATE TABLE IF NOT EXISTS aturan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    penyakit_id INTEGER,
    gejala_id INTEGER,
    pakar_cf FLOAT,
    FOREIGN KEY (penyakit_id) REFERENCES penyakit(id),
    FOREIGN KEY (gejala_id) REFERENCES gejala(id)
);

-- 4. Table: users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(35) UNIQUE NOT NULL,
    hashed_password VARCHAR(64) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    is_active BOOLEAN DEFAULT 1,
    alamat TEXT
);

-- 5. Table: diagnosa_history
CREATE TABLE IF NOT EXISTS diagnosa_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    penyakit_id INTEGER,
    faktor_kepastian FLOAT,
    persentase FLOAT,
    gejala_input TEXT,
    created_at VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (penyakit_id) REFERENCES penyakit(id)
);

-- Sample Data (Seed)
-- Note: These IDs assume starting from 1

-- Admin User (Password: indraaja)
INSERT INTO users (username, hashed_password, role, alamat) VALUES 
('indraaja', '$2b$12$K.z/M6.08Rz9O55.v8/8.O', 'admin', 'Jl. Admin No. 1');

-- Penyakit
INSERT INTO penyakit (id, nama, deskripsi, solusi, url_gambar) VALUES 
(1, 'Bekicot', 'Bekicot (Achatina fulica) merupakan hama penting yang menyerang tanaman kangkung dengan memakan daun dan batang muda. Serangan biasanya terjadi secara masif pada malam hari atau kondisi lingkungan yang sangat lembab, meninggalkan lubang-lubang besar yang tidak beraturan serta jejak lendir mengkilap pada permukaan tanaman.', 'Lakukan pencarian secara manual pada malam hari untuk mengumpulkan dan memusnahkan bekicot secara langsung. Taburkan abu kayu, serbuk gergaji, pasir kasar, atau pecahan cangkang telur di sekeliling bedengan tanaman sebagai penghalang fisik agar bekicot tidak mendekat. Gunakan umpan siput (moluskisida) berbahan aktif metaldehida secara bijaksana dan sesuai dosis anjuran jika serangan sudah melebihi batas kendali.', '/static/img/alternaria.png'),
(2, 'Ulat Grayak', 'Ulat Grayak (Spodoptera litura) adalah larva serangga yang sangat rakus dan merusak daun kangkung secara berkelompok. Hama ini aktif memakan helaian daun mulai dari tepi hingga menyisakan tulang daunnya saja, terutama di malam hari, sehingga mengganggu proses fotosintesis secara drastis.', 'Lakukan sanitasi lahan secara rutin dengan membersihkan gulma yang dapat menjadi tempat persembunyian ulat grayak. Kumpulkan kelompok telur dan ulat kecil yang ditemukan pada permukaan bawah daun lalu musnahkan segera. Semprotkan insektisida nabati berbasis minyak mimba atau Beauveria bassiana secara merata di sore hari, atau gunakan insektisida kimia berbahan aktif deltametrin jika populasi hama sangat tinggi.', '/static/img/alternaria.png'),
(3, 'Kutu Daun', 'Kutu Daun (Aphids) adalah serangga kecil penghisap cairan sel tanaman kangkung, biasanya mengelompok di bagian bawah daun atau pucuk muda. Serangan hama ini menyebabkan helaian daun mengkerut, melengkung, menguning, dan tanaman tumbuh kerdil, serta dapat menularkan penyakit virus lainnya.', 'Semprot tanaman kangkung menggunakan air bertekanan kuat secara rutin untuk meluruhkan koloni kutu daun dari permukaan daun. Aplikasikan sabun insektisida organik atau minyak mimba secara berkala pada bagian bawah daun yang terserang. Pasang perangkap kartu kuning lengket di sekitar lahan untuk memantau dan meminimalkan populasi kutu daun dewasa.', '/static/img/virus-mosaik.png'),
(4, 'Ulat Keket', 'Ulat Keket atau ulat tanduk merupakan larva berukuran besar dari ngengat Agrius convolvuli yang memakan daun kangkung dengan sangat cepat. Akibat gigitannya, daun kangkung dapat rusak parah dan bahkan menyisakan batangnya saja dalam beberapa hari jika tidak segera ditangani.', 'Lakukan pemantauan intensif pada pagi dan sore hari untuk menemukan ulat keket secara manual karena ukurannya yang besar memudahkan pengamatan fisik. Pungut ulat tersebut langsung dari batang kangkung dan musnahkan. Jika serangan meluas, semprot tanaman dengan insektisida hayati berbahan aktif Bacillus thuringiensis yang sangat efektif mengendalikan ulat daun.', '/static/img/alternaria.png'),
(5, 'Karat Putih', 'Karat Putih adalah penyakit yang disebabkan oleh oomycete Albugo ipomoeae-panduratae. Penyakit ini menyerang daun kangkung dengan memicu bintik kuning di permukaan atas dan pustula putih berkapur di permukaan bawah daun, sehingga menurunkan kualitas panen secara signifikan.', 'Cabut dan musnahkan daun atau tanaman kangkung yang terinfeksi karat putih untuk memutus siklus penyebaran spora melalui angin. Atur jarak tanam kangkung minimal 15-20 cm untuk menjaga sirkulasi udara di sekitar tajuk daun tetap optimal. Aplikasikan fungisida berbasis sulfur secara berkala atau gunakan fungisida berbahan aktif tembaga oksida sesuai anjuran jika infeksi meluas.', '/static/img/karat-putih.png'),
(6, 'Bercak Daun', 'Penyakit bercak daun kangkung ditandai dengan munculnya noda atau bercak kecokelatan hingga kehitaman pada permukaan daun. Infeksi jamur ini berkembang sangat pesat pada cuaca hangat dan kelembaban udara yang tinggi, yang mengakibatkan daun layu dan gugur sebelum waktunya.', 'Pangkas daun yang menunjukkan gejala bercak kecokelatan dan jaga kebersihan area lahan dari serpihan sisa tanaman yang gugur. Hindari penyiraman di sore hari secara langsung pada daun dan lebih baik lakukan penyiraman pada area perakaran di pagi hari. Gunakan fungisida organik berbahan ekstrak bawang putih atau semprotkan fungisida mankozeb sesuai dosis anjuran.', '/static/img/Cercospora.png'),
(7, 'Bakteri', 'Penyakit bakteri menyerang jaringan vaskular tanaman kangkung, menyebabkan batang membubur lunak, mengeluarkan lendir keruh dari jaringan yang terinfeksi, serta mengeluarkan aroma busuk yang sangat menyengat.', 'Segera cabut tanaman kangkung yang membusuk beserta tanah perakarannya lalu bakar di luar area budidaya untuk mencegah kontaminasi tanah. Pastikan sistem drainase lahan berjalan dengan baik sehingga tidak terjadi genangan air yang memicu perkembangbiakan bakteri patogen. Gunakan bakterisida berbahan aktif tembaga hidroksida untuk mensterilkan tanaman di sekitarnya.', '/static/img/busuk-akar-pythium.png'),
(8, 'Virus', 'Penyakit virus mosaik kangkung ditandai dengan pola warna belang hijau tua dan hijau muda yang tidak teratur, daun menguning pekat, keriput, batang mengalami bercak-bercak, serta tanaman tumbuh sangat kerdil.', 'Eradikasi atau cabut dan bakar seluruh tanaman kangkung yang bergejala mosaik untuk mencegah penyebaran virus ke tanaman sehat lainnya. Kendalikan populasi serangga vektor penular seperti kutu daun dengan menyemprotkan sabun insektisida atau minyak mimba secara berkala. Selalu lakukan sterilisasi peralatan pertanian menggunakan alkohol sebelum digunakan berpindah tanaman.', '/static/img/virus-mosaik.png'),
(9, 'Alga', 'Penyakit alga merah dipicu oleh organisme Cephaleuros virescens. Penyakit ini memicu bercak karat merah atau kelabu kehijauan pada daun kangkung, disertai dengan pertumbuhan rambut halus cokelat kemerahan di permukaannya.', 'Lakukan pemangkasan pada daun-daun kangkung yang tua atau bagian tanaman terbawah yang terlalu lembab untuk meminimalkan paparan spora alga. Pastikan lahan terpapar sinar matahari secara penuh dan hindari tingkat kerapatan tanaman yang berlebihan. Lakukan penyemprotan fungisida berbahan aktif tembaga jika tingkat serangan alga merusak sebagian besar dedaunan.', '/static/img/embun-bulu.png');

-- Gejala
INSERT INTO gejala (id, kode, deskripsi) VALUES 
(1, 'G001', 'Batang dan daun rusak'),
(2, 'G002', 'Batang dan daun layu'),
(3, 'G003', 'Batang dan daun busuk'),
(4, 'G004', 'Daun berlubang'),
(5, 'G005', 'Pinggir daun bergerigi'),
(6, 'G006', 'Tanaman kerdil'),
(7, 'G007', 'Daun melengkung'),
(8, 'G008', 'Warna daun hijau muda dengan garis menyilang kuning'),
(9, 'G009', 'Muncul bercak putih pada permukaan daun'),
(10, 'G010', 'Muncul bercak kecokelatan hingga kehitaman pada permukaan daun'),
(11, 'G011', 'Mengeluarkan lendir keruh'),
(12, 'G012', 'Berbau busuk'),
(13, 'G013', 'Keluar air pada batang'),
(14, 'G014', 'Lengket jika disentuh'),
(15, 'G015', 'Daun berwarna kuning pekat'),
(16, 'G016', 'Batang mengalami bercak-bercak'),
(17, 'G017', 'Daun menjadi seperti terbakar'),
(18, 'G018', 'Bentuk daun menjadi tidak sempurna'),
(19, 'G019', 'Daun layu'),
(20, 'G020', 'Bercak berwarna kelabu kehijauan pada daun'),
(21, 'G021', 'Pada permukaan tumbuh rambut berwarna cokelat kemerahan'),
(22, 'G022', 'Daun dihinggapi lalat'),
(23, 'G023', 'Batang dan daun kering'),
(24, 'G024', 'Bercak karat merah pada daun');

-- Aturan
INSERT INTO aturan (penyakit_id, gejala_id, pakar_cf) VALUES 
(1, 1, 1.0),
(1, 2, 1.0),
(1, 3, 1.0),
(2, 1, 1.0),
(2, 4, 1.0),
(2, 5, 1.0),
(3, 6, 1.0),
(3, 7, 1.0),
(4, 1, 1.0),
(4, 4, 1.0),
(4, 8, 1.0),
(5, 1, 1.0),
(5, 9, 1.0),
(6, 1, 1.0),
(6, 10, 1.0),
(7, 11, 1.0),
(7, 12, 1.0),
(7, 14, 1.0),
(8, 16, 1.0),
(8, 17, 1.0),
(8, 18, 1.0),
(9, 20, 1.0),
(9, 21, 1.0),
(9, 24, 1.0);
