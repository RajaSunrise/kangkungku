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
    admin_user = models.User(username="indraaja", email="admin@kangkung.com", hashed_password=admin_password, role="admin")
    db.add(admin_user)

    # Create User
    user_password = get_password_hash("user1234")
    regular_user = models.User(username="user123", email="user@example.com", hashed_password=user_password, role="user")
    db.add(regular_user)

    db.commit()
    print("User admin dan user biasa dibuat.")

    # Diseases (15)
    data_penyakit = [
        {
            "nama": "Karat Putih (White Rust)",
            "nama_ilmiah": "Albugo ipomoeae-panduratae",
            "deskripsi": "Karat Putih adalah penyakit yang disebabkan oleh oomycete Albugo ipomoeae-panduratae. Penyakit ini sangat umum terjadi pada tanaman kangkung, terutama di lingkungan dengan kelembaban tinggi dan sirkulasi udara yang buruk. Penyakit ini tidak hanya menyerang daun tetapi dapat menyebar ke batang jika tidak segera ditangani. Gejala awal dimulai dengan bintik kuning kecil di permukaan atas daun, yang kemudian diikuti oleh munculnya pustula putih berkapur di bagian bawah daun. Jika dibiarkan, tanaman akan mengalami hambatan pertumbuhan yang signifikan.",
            "solusi": "[TINDAKAN SEGERA] Segera cabut dan musnahkan daun atau bagian tanaman yang memiliki pustula putih untuk mencegah penyebaran spora melalui angin atau percikan air. [PENGOBATAN] Gunakan fungisida organik berbasis sulfur atau semprotan air rebusan daun sirih sebagai antiseptik alami. Jika serangan sudah mencapai lebih dari 30% area tanam, gunakan fungisida berbahan aktif tembaga oksida atau klorotalonil sesuai dosis anjuran. [PENCEGAHAN] Atur jarak tanam minimal 15-20 cm untuk sirkulasi udara yang baik. Hindari penyiraman langsung pada daun di sore hari (lebih baik siram di area akar). Lakukan rotasi tanaman dengan jenis tanaman non-konvensional setiap 2 musim tanam.",
            "url_gambar": "/static/img/karat-putih.png"
        },
        {
            "nama": "Bercak Daun Cercospora",
            "nama_ilmiah": "Cercospora ipomoeae",
            "deskripsi": "Bercak daun ini disebabkan oleh jamur Cercospora yang berkembang pesat pada cuaca hangat dan lembab. Penyakit ini menyebabkan bercak nekrotik yang dapat menurunkan kapasitas fotosintesis tanaman secara drastis. Jika infeksi parah, seluruh daun dapat menguning dan gugur sebelum waktunya, yang berujung pada penurunan hasil panen yang signifikan. Jamur ini dapat bertahan hidup pada sisa-sisa tanaman di tanah selama berbulan-bulan.",
            "solusi": "[TINDAKAN SEGERA] Pangkas daun yang terinfeksi dan jangan biarkan jatuh ke tanah karena spora dapat bertahan di sisa tanaman. [PENGOBATAN] Aplikasikan fungisida sistemik berbahan aktif benomil atau mankozeb. Untuk solusi organik, gunakan ekstrak bawang putih yang diencerkan sebagai fungisida alami setiap 3 hari sekali. [PENCEGAHAN] Pastikan lahan memiliki drainase yang baik agar air tidak menggenang. Jaga kebersihan lahan dari gulma yang bisa menjadi inang alternatif. Gunakan pupuk kalium yang cukup untuk memperkuat dinding sel tanaman terhadap serangan jamur.",
            "url_gambar": "/static/img/cercospora.png"
        },
        {
            "nama": "Virus Mosaik Kangkung",
            "nama_ilmiah": "Water spinach mosaic virus",
            "deskripsi": "Virus ini merupakan salah satu ancaman paling serius karena tidak dapat diobati dengan pestisida. Virus mosaik biasanya ditularkan oleh serangga vektor seperti kutu daun (aphids) atau melalui alat pertanian yang tidak steril. Gejala yang paling khas adalah pola warna belang hijau tua dan muda yang tidak teratur pada daun, serta bentuk daun yang mengerut atau abnormal. Tanaman yang terinfeksi akan tumbuh sangat kerdil dan tidak layak dikonsumsi.",
            "solusi": "[TINDAKAN SEGERA] Cabut seluruh tanaman yang menunjukkan gejala mosaik hingga akarnya, masukkan ke dalam plastik, dan bakar di luar area lahan. JANGAN dijadikan kompos. [KONTROL VEKTOR] Fokus utama adalah membasmi kutu daun menggunakan sabun insektisida, minyak mimba (neem oil), atau insektisida berbahan aktif abamektin jika populasi serangga sangat tinggi. [PENCEGAHAN] Selalu sterilisasi alat potong menggunakan alkohol 70% sebelum berpindah ke tanaman lain. Gunakan benih bersertifikat yang bebas virus. Pasang perangkap kuning berperekat untuk memantau keberadaan serangga vektor.",
            "url_gambar": "/static/img/virus-mosaik.png"
        },
        {
            "nama": "Layu Fusarium",
            "nama_ilmiah": "Fusarium oxysporum",
            "deskripsi": "Layu Fusarium adalah penyakit tular tanah (soil-borne) yang menyerang sistem pembuluh tanaman. Jamur ini menyumbat aliran air dan nutrisi dari akar ke daun, sehingga tanaman tampak layu meskipun tanah cukup basah. Ciri khasnya adalah tanaman layu saat terik matahari tetapi segar kembali pada malam hari, hingga akhirnya mati secara permanen. Jika batang dipotong melintang, akan terlihat cincin kecoklatan pada jaringan pembuluhnya.",
            "solusi": "[TINDAKAN SEGERA] Singkirkan tanaman mati beserta tanah di sekeliling perakarannya untuk meminimalisir penyebaran spora di tanah. [PENGOBATAN TANAH] Gunakan agen hayati Trichoderma harzianum yang dicampurkan ke dalam kompos atau tanah sebelum tanam untuk menekan pertumbuhan jamur jahat. [PENCEGAHAN] Lakukan pengapuran tanah (dolomit) untuk menaikkan pH tanah menjadi 6.5-7.0, karena Fusarium menyukai tanah asam. Hindari penggunaan pupuk Urea berlebihan karena dapat memicu perkembangan jamur ini. Gunakan sistem irigasi yang tidak menyebabkan erosi tanah antar tanaman.",
            "url_gambar": "/static/img/layu-fusarium.png"
        },
        {
            "nama": "Busuk Akar Pythium",
            "nama_ilmiah": "Pythium spp.",
            "deskripsi": "Pythium sering disebut sebagai 'penyakit rebah kecambah' atau 'busuk akar' yang sangat merusak pada kondisi tanah jenuh air (becek). Jamur ini menyerang akar halus kangkung, membuatnya membusuk dan tidak mampu menyerap nutrisi. Pada bibit muda, pangkal batang akan menjadi lunak dan tanaman akan rebah seketika. Pada tanaman dewasa, pertumbuhan akan berhenti total dan daun menguning pucat.",
            "solusi": "[TINDAKAN SEGERA] Hentikan penyiraman segera dan perbaiki saluran drainase agar tidak ada air menggenang. [PENGOBATAN] Gunakan fungisida khusus oomycetes berbahan aktif metalaksil atau propamokarb hidroklorida. Untuk pencegahan alami, pastikan media tanam sudah difermentasi sempurna sebelum digunakan. [PENCEGAHAN] Pastikan benih ditanam pada kedalaman yang tepat (jangan terlalu dalam). Gunakan air siraman yang bersih (bukan air limbah atau air selokan yang terkontaminasi). Perkaya tanah dengan bahan organik untuk meningkatkan porositas tanah.",
            "url_gambar": "/static/img/busuk-akar-pythium.png"
        },
        {
            "nama": "Busuk Batang Rhizoctonia",
            "nama_ilmiah": "Rhizoctonia solani",
            "deskripsi": "Busuk batang Rhizoctonia adalah penyakit jamur tular tanah yang sering menyerang tanaman kangkung di lahan yang terlalu basah. Jamur ini menyerang pangkal batang, menciptakan lesi berwarna coklat kemerahan yang perlahan melingkari batang (girdling). Akibatnya, transportasi air terputus dan tanaman akan roboh atau mati mendadak. Penyakit ini sering muncul setelah hujan terus-menerus.",
            "solusi": "[TINDAKAN SEGERA] Segera kurangi frekuensi penyiraman dan lakukan pendangiran (penggemburan tanah) di sekitar batang untuk mengurangi kelembaban permukaan. [PENGOBATAN] Kocor pangkal batang dengan fungisida berbahan aktif benomil atau pcb (pencycuron). Secara organik, taburkan abu kayu di sekitar pangkal batang untuk menghambat jamur. [PENCEGAHAN] Gunakan benih yang sehat dan telah diberi perlakuan (seed treatment). Jangan menanam kangkung terlalu rapat. Pastikan sisa-sisa tanaman dari musim sebelumnya telah dibersihkan sepenuhnya.",
            "url_gambar": "/static/img/rhizoctonia.png"
        },
        {
            "nama": "Bercak Daun Alternaria",
            "nama_ilmiah": "Alternaria spp.",
            "deskripsi": "Penyakit ini ditandai dengan bercak daun yang memiliki pola cincin konsentris (seperti papan target). Penyakit ini berkembang pesat pada kondisi cuaca yang berganti-ganti antara basah dan kering. Jika dibiarkan, bercak-bercak ini akan menyatu dan menyebabkan hawar daun (leaf blight), di mana daun akan mengering seperti terbakar dan rontok.",
            "solusi": "[TINDAKAN SEGERA] Buang daun-daun tua di bagian bawah yang pertama kali menunjukkan gejala karena ini adalah sumber inokulum utama. [PENGOBATAN] Semprotkan fungisida kontak berbahan aktif klorotalonil atau propineb. Untuk pengobatan organik, semprotkan larutan baking soda (1 sendok teh per liter air) yang dicampur sedikit sabun cair sebagai fungisida kontak. [PENCEGAHAN] Hindari penggunaan sistem irigasi pancar (overhead irrigation). Lakukan pemupukan berimbang, pastikan tanaman mendapatkan cukup unsur mikro (seperti Boron dan Zink) untuk daya tahan daun.",
            "url_gambar": "/static/img/alternaria.png"
        },
        {
            "nama": "Bercak Daun Bakteri",
            "nama_ilmiah": "Pseudomonas / Xanthomonas",
            "deskripsi": "Berbeda dengan jamur, bercak daun bakteri biasanya terlihat 'basah' atau berminyak. Bakteri ini masuk melalui luka atau pori-pori alami tanaman (hidatoda) saat kelembaban sangat tinggi. Ciri khasnya adalah adanya 'halo' kuning di sekitar bercak gelap. Bakteri ini sangat cepat menyebar melalui percikan air hujan atau alat pertanian yang terkontaminasi.",
            "solusi": "[TINDAKAN SEGERA] Hentikan semua kegiatan di lahan saat tanaman basah (setelah hujan/siram) untuk mencegah penyebaran bakteri lewat tangan atau baju. [PENGOBATAN] Gunakan bakterisida atau fungisida berbahan aktif tembaga (Copper) seperti tembaga hidroksida yang efektif menekan bakteri. Belum ada obat organik yang sangat efektif, namun larutan kunyit bisa dicoba sebagai bakterisida alami ringan. [PENCEGAHAN] Gunakan benih bebas bakteri. Desinfeksi semua alat potong menggunakan alkohol atau larutan pemutih encer. Atur drainase agar tidak terjadi kelembaban udara yang ekstrim di area pertanaman.",
            "url_gambar": "/static/img/bakteri.png"
        },
        {
            "nama": "Embun Tepung (Powdery Mildew)",
            "nama_ilmiah": "Erysiphe spp.",
            "deskripsi": "Embun tepung mudah dikenali dari lapisan putih seperti tepung atau bedak di permukaan atas daun. Penyakit ini unik karena justru sering berkembang pada kondisi udara kering namun dengan kelembaban tinggi di sekitar tanaman. Lapisan putih ini sebenarnya adalah koloni jamur yang menyerap nutrisi langsung dari sel epidermis daun, menyebabkan daun mengerut dan fotosintesis terhenti.",
            "solusi": "[TINDAKAN SEGERA] Semprot tanaman dengan air bertekanan kuat di pagi hari untuk merontokkan spora tepung secara fisik. [PENGOBATAN] Gunakan fungisida sistemik berbahan aktif tebukonazol. Secara organik, semprotan campuran susu cair dan air (rasio 1:9) sangat efektif karena protein dalam susu akan bereaksi dengan sinar matahari menjadi antiseptik bagi jamur ini. [PENCEGAHAN] Tanam kangkung di lokasi yang mendapatkan sinar matahari penuh minimal 6-8 jam sehari. Jangan memberikan pupuk nitrogen terlalu tinggi karena jaringan tanaman yang terlalu sukulen lebih mudah diserang.",
            "url_gambar": "/static/img/embun-tepung.png"
        },
        {
            "nama": "Embun Bulu (Downy Mildew)",
            "nama_ilmiah": "Peronospora spp.",
            "deskripsi": "Downy mildew sering tertukar dengan powdery mildew, namun jamur ini tumbuh di bagian bawah daun dengan tekstur berbulu halus berwarna keunguan atau abu-abu. Di permukaan atas daun hanya terlihat bercak kuning pucat yang dibatasi oleh tulang daun (berbentuk menyudut). Penyakit ini sangat berbahaya pada cuaca dingin dan berkabut.",
            "solusi": "[TINDAKAN SEGERA] Buang segera daun yang menunjukkan bercak kuning menyudut. Perbaiki sirkulasi udara dengan membuang gulma di sekitar bedengan. [PENGOBATAN] Gunakan fungisida khusus oomycetes seperti yang digunakan untuk Pythium (Metalaksil atau Dimetomorf). Untuk cara organik, gunakan semprotan rebusan batang serai yang mengandung sitronela sebagai antijamur. [PENCEGAHAN] Hindari menanam kangkung di area yang ternaungi atau selalu lembab. Pastikan sisa tanaman musim lalu dibakar untuk memutus siklus spora dorman.",
            "url_gambar": "/static/img/embun-bulu.png"
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
        {"kode": "G01", "deskripsi": "Bercak putih menonjol pada sisi bawah daun"},
        {"kode": "G02", "deskripsi": "Bercak kuning pada sisi atas daun"},
        {"kode": "G03", "deskripsi": "Daun melengkung atau terdistorsi"},
        {"kode": "G04", "deskripsi": "Bercak bulat dengan pusat abu-abu/putih"},
        {"kode": "G05", "deskripsi": "Bercak dengan tepi coklat tua/merah"},
        {"kode": "G06", "deskripsi": "Pola mosaik hijau terang/gelap pada daun"},
        {"kode": "G07", "deskripsi": "Pertumbuhan tanaman kerdil"},
        {"kode": "G08", "deskripsi": "Daun bagian bawah menguning"},
        {"kode": "G09", "deskripsi": "Tanaman layu pada siang hari, pulih malam hari"},
        {"kode": "G10", "deskripsi": "Jaringan pembuluh batang berwarna coklat"},
        {"kode": "G11", "deskripsi": "Akar berwarna coklat dan lembek"},
        {"kode": "G12", "deskripsi": "Batang lunak dan gelap di dekat tanah"},
        {"kode": "G13", "deskripsi": "Lesi cekung kemerahan pada batang"},
        {"kode": "G14", "deskripsi": "Bercak seperti target dengan cincin konsentris"},
        {"kode": "G15", "deskripsi": "Bercak basah dikelilingi halo kuning"},
        {"kode": "G16", "deskripsi": "Serbuk putih pada permukaan daun"},
        {"kode": "G17", "deskripsi": "Pertumbuhan berbulu halus abu-abu/ungu di bawah daun"},
        {"kode": "G24", "deskripsi": "Daun berlubang (shot-holes)"}
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
        # White Rust
        ("Karat Putih (White Rust)", "G01", 0.9),
        ("Karat Putih (White Rust)", "G02", 0.7),
        ("Karat Putih (White Rust)", "G03", 0.5),

        # Cercospora Leaf Spot
        ("Bercak Daun Cercospora", "G04", 0.8),
        ("Bercak Daun Cercospora", "G05", 0.8),
        ("Bercak Daun Cercospora", "G08", 0.4),

        # Mosaic Virus
        ("Virus Mosaik Kangkung", "G06", 0.95),
        ("Virus Mosaik Kangkung", "G03", 0.6),
        ("Virus Mosaik Kangkung", "G07", 0.7),

        # Fusarium Wilt
        ("Layu Fusarium", "G08", 0.6),
        ("Layu Fusarium", "G09", 0.9),
        ("Layu Fusarium", "G10", 0.8),
        ("Layu Fusarium", "G07", 0.5),

        # Pythium Root Rot
        ("Busuk Akar Pythium", "G11", 0.9),
        ("Busuk Akar Pythium", "G07", 0.6),
        ("Busuk Akar Pythium", "G09", 0.5),

        # Rhizoctonia Stem Rot
        ("Busuk Batang Rhizoctonia", "G12", 0.8),
        ("Busuk Batang Rhizoctonia", "G13", 0.9),
        ("Busuk Batang Rhizoctonia", "G09", 0.4),

        # Alternaria Leaf Spot
        ("Bercak Daun Alternaria", "G14", 0.9),
        ("Bercak Daun Alternaria", "G08", 0.5),

        # Bacterial Leaf Spot
        ("Bercak Daun Bakteri", "G15", 0.9),
        ("Bercak Daun Bakteri", "G24", 0.7),
        ("Bercak Daun Bakteri", "G08", 0.4),

        # Powdery Mildew
        ("Embun Tepung (Powdery Mildew)", "G16", 0.95),
        ("Embun Tepung (Powdery Mildew)", "G03", 0.5),

        # Downy Mildew
        ("Embun Bulu (Downy Mildew)", "G17", 0.9),
        ("Embun Bulu (Downy Mildew)", "G02", 0.6),
        ("Embun Bulu (Downy Mildew)", "G08", 0.5),
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
