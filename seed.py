from app.database import SessionLocal, engine
from app import models
from app.security import get_password_hash

def tebar():
    db = SessionLocal()

    # Create tables
    models.Base.metadata.create_all(bind=engine)

    # Clear existing data
    db.query(models.DiagnosaHistory).delete()
    db.query(models.Aturan).delete()
    db.query(models.Gejala).delete()
    db.query(models.Penyakit).delete()
    db.query(models.User).delete()
    db.commit()

    print("Data lama dihapus.")

    # Create Admin
    admin_password = get_password_hash("indraaja")
    admin_user = models.User(username="indraaja", email="admin@kangkung.com", hashed_password=admin_password, role="admin", alamat="Jl. Admin No. 1")
    db.add(admin_user)

    # Create User
    user_password = get_password_hash("user1234")
    regular_user = models.User(username="user123", email="user@example.com", hashed_password=user_password, role="user", alamat="Jl. User No. 2")
    db.add(regular_user)

    db.commit()
    print("User admin dan user biasa dibuat.")

    # Diseases (15)
    data_penyakit = [
        {
            'nama': 'Karat Putih (White Rust)',
            'nama_ilmiah': 'Albugo ipomoeae-panduratae',
            'deskripsi': 'Karat Putih adalah penyakit yang disebabkan oleh oomycete Albugo ipomoeae-panduratae. Penyakit ini sangat umum terjadi pada tanaman kangkung, terutama di lingkungan dengan kelembaban tinggi dan sirkulasi udara yang buruk. Penyakit ini tidak hanya menyerang daun tetapi dapat menyebar ke batang jika tidak segera ditangani. Gejala awal dimulai dengan bintik kuning kecil di permukaan atas daun, yang kemudian diikuti oleh munculnya pustula putih berkapur di bagian bawah daun. Jika dibiarkan, tanaman akan mengalami hambatan pertumbuhan yang signifikan.',
            'solusi': '[TINDAKAN SEGERA] Segera cabut dan musnahkan daun atau bagian tanaman yang memiliki pustula putih untuk mencegah penyebaran spora melalui angin atau percikan air. [PENGOBATAN] Gunakan fungisida organik berbasis sulfur atau semprotan air rebusan daun sirih sebagai antiseptik alami. Jika serangan sudah mencapai lebih dari 30% area tanam, gunakan fungisida berbahan aktif tembaga oksida atau klorotalonil sesuai dosis anjuran. [PENCEGAHAN] Atur jarak tanam minimal 15-20 cm untuk sirkulasi udara yang baik. Hindari penyiraman langsung pada daun di sore hari (lebih baik siram di area akar). Lakukan rotasi tanaman dengan jenis tanaman non-konvensional setiap 2 musim tanam.',
            'url_gambar': '/static/img/karat-putih.png'
        },
        {
            'nama': 'Bercak Daun Cercospora',
            'nama_ilmiah': 'Cercospora ipomoeae',
            'deskripsi': 'Bercak daun ini disebabkan oleh jamur Cercospora yang berkembang pesat pada cuaca hangat dan lembab. Penyakit ini menyebabkan bercak nekrotik yang dapat menurunkan kapasitas fotosintesis tanaman secara drastis. Jika infeksi parah, seluruh daun dapat menguning dan gugur sebelum waktunya, yang berujung pada penurunan hasil panen yang signifikan. Jamur ini dapat bertahan hidup pada sisa-sisa tanaman di tanah selama berbulan-bulan.',
            'solusi': '[TINDAKAN SEGERA] Pangkas daun yang terinfeksi dan jangan biarkan jatuh ke tanah karena spora dapat bertahan di sisa tanaman. [PENGOBATAN] Aplikasikan fungisida sistemik berbahan aktif benomil atau mankozeb. Untuk solusi organik, gunakan ekstrak bawang putih yang diencerkan sebagai fungisida alami setiap 3 hari sekali. [PENCEGAHAN] Pastikan lahan memiliki drainase yang baik agar air tidak menggenang. Jaga kebersihan lahan dari gulma yang bisa menjadi inang alternatif. Gunakan pupuk kalium yang cukup untuk memperkuat dinding sel tanaman terhadap serangan jamur.',
            'url_gambar': '/static/img/cercospora.png'
        },
        {
            'nama': 'Virus Mosaik Kangkung',
            'nama_ilmiah': 'Water spinach mosaic virus',
            'deskripsi': 'Virus ini merupakan salah satu ancaman paling serius karena tidak dapat diobati dengan pestisida. Virus mosaik biasanya ditularkan oleh serangga vektor seperti kutu daun (aphids) atau melalui alat pertanian yang tidak steril. Gejala yang paling khas adalah pola warna belang hijau tua dan muda yang tidak teratur pada daun, serta bentuk daun yang mengerut atau abnormal. Tanaman yang terinfeksi akan tumbuh sangat kerdil dan tidak layak dikonsumsi.',
            'solusi': '[TINDAKAN SEGERA] Cabut seluruh tanaman yang menunjukkan gejala mosaik hingga akarnya, masukkan ke dalam plastik, dan bakar di luar area lahan. JANGAN dijadikan kompos. [KONTROL VEKTOR] Fokus utama adalah membasmi kutu daun menggunakan sabun insektisida, minyak mimba (neem oil), atau insektisida berbahan aktif abamektin jika populasi serangga sangat tinggi. [PENCEGAHAN] Selalu sterilisasi alat potong menggunakan alkohol 70% sebelum berpindah ke tanaman lain. Gunakan benih bersertifikat yang bebas virus. Pasang perangkap kuning berperekat untuk memantau keberadaan serangga vektor.',
            'url_gambar': '/static/img/mosaik.png'
        },
        {
            'nama': 'Layu Fusarium',
            'nama_ilmiah': 'Fusarium oxysporum',
            'deskripsi': 'Layu Fusarium adalah penyakit tular tanah (soil-borne) yang menyerang sistem pembuluh tanaman. Jamur ini menyumbat aliran air dan nutrisi dari akar ke daun, sehingga tanaman tampak layu meskipun tanah cukup basah. Ciri khasnya adalah tanaman layu saat terik matahari tetapi segar kembali pada malam hari, hingga akhirnya mati secara permanen. Jika batang dipotong melintang, akan terlihat cincin kecoklatan pada jaringan pembuluhnya.',
            'solusi': '[TINDAKAN SEGERA] Singkirkan tanaman mati beserta tanah di sekeliling perakarannya untuk meminimalisir penyebaran spora di tanah. [PENGOBATAN TANAH] Gunakan agen hayati Trichoderma harzianum yang dicampurkan ke dalam kompos atau tanah sebelum tanam untuk menekan pertumbuhan jamur jahat. [PENCEGAHAN] Lakukan pengapuran tanah (dolomit) untuk menaikkan pH tanah menjadi 6.5-7.0, karena Fusarium menyukai tanah asam. Hindari penggunaan pupuk Urea berlebihan karena dapat memicu perkembangan jamur ini. Gunakan sistem irigasi yang tidak menyebabkan erosi tanah antar tanaman.',
            'url_gambar': '/static/img/fusarium.png'
        },
        {
            'nama': 'Busuk Akar Pythium',
            'nama_ilmiah': 'Pythium spp',
            'deskripsi': 'Pythium sering disebut sebagai \'penyakit rebah kecambah\' atau \'busuk akar\' yang sangat merusak pada kondisi tanah jenuh air (becek). Jamur ini menyerang akar halus kangkung, membuatnya membusuk dan tidak mampu menyerap nutrisi. Pada bibit muda, pangkal batang akan menjadi lunak dan tanaman akan rebah seketika. Pada tanaman dewasa, pertumbuhan akan berhenti total dan daun menguning pucat.',
            'solusi': '[TINDAKAN SEGERA] Hentikan penyiraman segera dan perbaiki saluran drainase agar tidak ada air menggenang. [PENGOBATAN] Gunakan fungisida khusus oomycetes berbahan aktif metalaksil atau propamokarb hidroklorida. Untuk pencegahan alami, pastikan media tanam sudah difermentasi sempurna sebelum digunakan. [PENCEGAHAN] Pastikan benih ditanam pada kedalaman yang tepat (jangan terlalu dalam). Gunakan air siraman yang bersih (bukan air limbah atau air selokan yang terkontaminasi). Perkaya tanah dengan bahan organik untuk meningkatkan porositas tanah.',
            'url_gambar': '/static/img/pythium.png'
        },
        {
            'nama': 'Busuk Batang Rhizoctonia',
            'nama_ilmiah': 'Rhizoctonia solani',
            'deskripsi': 'Busuk batang Rhizoctonia adalah penyakit jamur tular tanah yang sering menyerang tanaman kangkung di lahan yang terlalu basah. Jamur ini menyerang pangkal batang, menciptakan lesi berwarna coklat kemerahan yang perlahan melingkari batang (girdling). Akibatnya, transportasi air terputus dan tanaman akan roboh atau mati mendadak. Penyakit ini sering muncul setelah hujan terus-menerus.',
            'solusi': '[TINDAKAN SEGERA] Segera kurangi frekuensi penyiraman dan lakukan pendangiran (penggemburan tanah) di sekitar batang untuk mengurangi kelembaban permukaan. [PENGOBATAN] Kocor pangkal batang dengan fungisida berbahan aktif benomil atau pcb (pencycuron). Secara organik, taburkan abu kayu di sekitar pangkal batang untuk menghambat jamur. [PENCEGAHAN] Gunakan benih yang sehat dan telah diberi perlakuan (seed treatment). Jangan menanam kangkung terlalu rapat. Pastikan sisa-sisa tanaman dari musim sebelumnya telah dibersihkan sepenuhnya.',
            'url_gambar': '/static/img/rhizoctonia.png'
        },
        {
            'nama': 'Embun Tepung (Powdery Mildew)',
            'nama_ilmiah': 'Erysiphe spp.',
            'deskripsi': 'Embun tepung mudah dikenali dari lapisan putih seperti tepung atau bedak di permukaan atas daun. Penyakit ini unik karena justru sering berkembang pada kondisi udara kering namun dengan kelembaban tinggi di sekitar tanaman. Lapisan putih ini sebenarnya adalah koloni jamur yang menyerap nutrisi langsung dari sel epidermis daun, menyebabkan daun mengerut dan fotosintesis terhenti.',
            'solusi': '[TINDAKAN SEGERA] Semprot tanaman dengan air bertekanan kuat di pagi hari untuk merontokkan spora tepung secara fisik. [PENGOBATAN] Gunakan fungisida sistemik berbahan aktif tebukonazol. Secara organik, semprotan campuran susu cair dan air (rasio 1:9) sangat efektif karena protein dalam susu akan bereaksi dengan sinar matahari menjadi antiseptik bagi jamur ini. [PENCEGAHAN] Tanam kangkung di lokasi yang mendapatkan sinar matahari penuh minimal 6-8 jam sehari. Jangan memberikan pupuk nitrogen terlalu tinggi karena jaringan tanaman yang terlalu sukulen lebih mudah diserang.',
            'url_gambar': '/static/img/embun-tepung.png'
        },
        {
            'nama': 'Embun Bulu (Downy Mildew)',
            'nama_ilmiah': 'Peronospora spp.',
            'deskripsi': 'Downy mildew sering tertukar dengan powdery mildew, namun jamur ini tumbuh di bagian bawah daun dengan tekstur berbulu halus berwarna keunguan atau abu-abu. Di permukaan atas daun hanya terlihat bercak kuning pucat yang dibatasi oleh tulang daun (berbentuk menyudut). Penyakit ini sangat berbahaya pada cuaca dingin dan berkabut.',
            'solusi': '[TINDAKAN SEGERA] Buang segera daun yang menunjukkan bercak kuning menyudut. Perbaiki sirkulasi udara dengan membuang gulma di sekitar bedengan. [PENGOBATAN] Gunakan fungisida khusus oomycetes seperti yang digunakan untuk Pythium (Metalaksil atau Dimetomorf). Untuk cara organik, gunakan semprotan rebusan batang serai yang mengandung sitronela sebagai antijamur. [PENCEGAHAN] Hindari menanam kangkung di area yang ternaungi atau selalu lembab. Pastikan sisa tanaman musim lalu dibakar untuk memutus siklus spora dorman.',
            'url_gambar': '/static/img/embun-bulu.png'
        },
    ]

    # Insert Diseases
    db_penyakit_list = []
    for d_data in data_penyakit:
        penyakit = models.Penyakit(**d_data)
        db.add(penyakit)
        db_penyakit_list.append(penyakit)
    db.commit()

    # Reload diseases to get IDs
    db_penyakit_list = db.query(models.Penyakit).all()
    map_penyakit = {p.nama: p.id for p in db_penyakit_list}

    # Symptoms
    data_gejala = [
        {"kode": "G001", "deskripsi": "Bercak putih menonjol pada sisi bawah daun"},
        {"kode": "G002", "deskripsi": "Bercak kuning pada sisi atas daun"},
        {"kode": "G003", "deskripsi": "Daun melengkung atau terdistorsi"},
        {"kode": "G004", "deskripsi": "Bercak bulat dengan pusat abu-abu/putih"},
        {"kode": "G005", "deskripsi": "Bercak dengan tepi coklat tua/merah"},
        {"kode": "G006", "deskripsi": "Pola mosaik hijau terang/gelap pada daun"},
        {"kode": "G007", "deskripsi": "Pertumbuhan tanaman kerdil"},
        {"kode": "G008", "deskripsi": "Daun bagian bawah menguning"},
        {"kode": "G009", "deskripsi": "Tanaman layu pada siang hari, pulih malam hari"},
        {"kode": "G010", "deskripsi": "Jaringan pembuluh batang berwarna coklat"},
        {"kode": "G011", "deskripsi": "Akar berwarna coklat dan lembe"},
        {"kode": "G012", "deskripsi": "Batang lunak dan gelap di dekat tanah"},
        {"kode": "G013", "deskripsi": "Lesi cekung kemerahan pada batang"},
        {"kode": "G014", "deskripsi": "Pertumbuhan berbulu halus abu-abu/ungu di bawah daun"},
        {"kode": "G015", "deskripsi": "Serbuk putih pada permukaan daun"},
    ]

    # Insert Symptoms
    db_gejala_list = []
    for g_data in data_gejala:
        gejala = models.Gejala(**g_data)
        db.add(gejala)
        db_gejala_list.append(gejala)
    db.commit()

    # Reload symptoms
    db_gejala_list = db.query(models.Gejala).all()
    map_gejala = {g.kode: g.id for g in db_gejala_list}

    # Rules (Disease Name, Symptom Code, Expert CF)
    data_aturan = [
        ("Karat Putih (White Rust)", "G001", 0.8),
        ("Karat Putih (White Rust)", "G002", 0.8),
        ("Karat Putih (White Rust)", "G003", 0.8),
        ("Bercak Daun Cercospora", "G004", 0.8),
        ("Bercak Daun Cercospora", "G005", 0.8),
        ("Bercak Daun Cercospora", "G008", 0.8),
        ("Virus Mosaik Kangkung", "G003", 0.8),
        ("Virus Mosaik Kangkung", "G006", 0.8),
        ("Virus Mosaik Kangkung", "G007", 0.8),
        ("Layu Fusarium", "G007", 0.8),
        ("Layu Fusarium", "G008", 0.8),
        ("Layu Fusarium", "G009", 0.8),
        ("Layu Fusarium", "G010", 0.8),
        ("Busuk Akar Pythium", "G007", 0.8),
        ("Busuk Akar Pythium", "G009", 0.8),
        ("Busuk Akar Pythium", "G011", 0.8),
        ("Busuk Batang Rhizoctonia", "G009", 0.8),
        ("Busuk Batang Rhizoctonia", "G012", 0.8),
        ("Busuk Batang Rhizoctonia", "G013", 0.8),
        ("Embun Tepung (Powdery Mildew)", "G003", 0.8),
        ("Embun Tepung (Powdery Mildew)", "G015", 0.8),
        ("Embun Bulu (Downy Mildew)", "G002", 0.8),
        ("Embun Bulu (Downy Mildew)", "G008", 0.8),
        ("Embun Bulu (Downy Mildew)", "G014", 0.8),
    ]

    # Insert Rules
    for nama_penyakit, kode_gejala, cf in data_aturan:
        penyakit_id = map_penyakit.get(nama_penyakit)
        gejala_id = map_gejala.get(kode_gejala)

        if penyakit_id and gejala_id:
            aturan = models.Aturan(penyakit_id=penyakit_id, gejala_id=gejala_id, pakar_cf=cf)
            db.add(aturan)

    db.commit()
    print("Database berhasil diisi!")
    db.close()

if __name__ == "__main__":
    tebar()
