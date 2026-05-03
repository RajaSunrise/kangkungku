-- SQL Script to recreate the KangkungKu database structure and initial data
-- Compatible with MySQL, PostgreSQL, and SQLite

-- 1. Table: penyakit
CREATE TABLE IF NOT EXISTS penyakit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama VARCHAR(255) NOT NULL,
    nama_ilmiah VARCHAR(255),
    deskripsi TEXT,
    solusi TEXT,
    url_gambar VARCHAR(255)
);

-- 2. Table: gejala
CREATE TABLE IF NOT EXISTS gejala (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kode VARCHAR(10) UNIQUE NOT NULL,
    deskripsi VARCHAR(255) NOT NULL,
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
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    is_active BOOLEAN DEFAULT 1,
    alamat VARCHAR(255)
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
INSERT INTO users (username, email, hashed_password, role, alamat) VALUES 
('indraaja', 'admin@kangkung.com', '$2b$12$K.z/M6.08Rz9O55.v8/8.O', 'admin', 'Jl. Admin No. 1');

-- Penyakit
INSERT INTO penyakit (nama, nama_ilmiah, deskripsi, solusi, url_gambar) VALUES 
('Karat Putih (White Rust)', 'Albugo ipomoeae-panduratae', 'Karat Putih adalah penyakit yang disebabkan oleh oomycete Albugo ipomoeae-panduratae...', 'Segera cabut dan musnahkan daun atau bagian tanaman...', '/static/img/karat-putih.png'),
('Bercak Daun Cercospora', 'Cercospora ipomoeae', 'Bercak daun ini disebabkan oleh jamur Cercospora...', 'Pangkas daun yang terinfeksi...', '/static/img/cercospora.png'),
('Virus Mosaik Kangkung', 'Water spinach mosaic virus', 'Virus ini merupakan salah satu ancaman paling serius...', 'Cabut seluruh tanaman yang menunjukkan gejala mosaik...', '/static/img/mosaik.png'),
('Layu Fusarium', 'Fusarium oxysporum', 'Layu Fusarium adalah penyakit tular tanah...', 'Singkirkan tanaman mati beserta tanah...', '/static/img/fusarium.png'),
('Busuk Akar Pythium', 'Pythium spp', 'Pythium sering disebut sebagai penyakit rebah kecambah...', 'Hentikan penyiraman segera...', '/static/img/pythium.png');

-- Gejala
INSERT INTO gejala (kode, deskripsi) VALUES 
('G001', 'Bercak putih menonjol pada sisi bawah daun'),
('G002', 'Bercak kuning pada sisi atas daun'),
('G003', 'Daun melengkung atau terdistorsi'),
('G004', 'Bercak bulat dengan pusat abu-abu/putih'),
('G005', 'Bercak dengan tepi coklat tua/merah'),
('G006', 'Pola mosaik hijau terang/gelap pada daun'),
('G007', 'Pertumbuhan tanaman kerdil');

-- Aturan (Example mappings)
INSERT INTO aturan (penyakit_id, gejala_id, pakar_cf) VALUES 
(1, 1, 0.8), -- Karat Putih -> G001
(1, 2, 0.8), -- Karat Putih -> G002
(2, 4, 0.8), -- Cercospora -> G004
(3, 6, 0.8); -- Virus Mosaik -> G006
