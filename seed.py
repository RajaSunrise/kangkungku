from app.database import SessionLocal, engine
from app import models

def tebar():
    db = SessionLocal()

    # Create tables
    models.Base.metadata.create_all(bind=engine)

    # Clear existing data
    db.query(models.Aturan).delete()
    db.query(models.Gejala).delete()
    db.query(models.Penyakit).delete()
    db.commit()

    print("Data lama dihapus.")

    # Diseases (15)
    data_penyakit = [
        {
            "nama": "Karat Putih (White Rust)",
            "nama_ilmiah": "Albugo ipomoeae-panduratae",
            "deskripsi": "Penyakit jamur yang menyebabkan pustula putih menonjol di bagian bawah daun. Pustula ini akhirnya pecah, melepaskan spora seperti bubuk putih. Permukaan atas daun mungkin menunjukkan bintik-bintik kuning yang sesuai dengan pustula di bawahnya. Infeksi parah dapat menyebabkan distorsi daun, pertumbuhan terhambat, dan kerontokan daun.",
            "solusi": "Segera buang dan musnahkan daun yang terinfeksi. Tingkatkan sirkulasi udara dengan memberi jarak tanam yang tepat. Hindari penyiraman dari atas untuk menjaga dedaunan tetap kering. Gunakan fungisida berbahan dasar tembaga atau klorotalonil jika infeksi parah. Rotasi tanaman dengan tanaman bukan inang disarankan.",
            "url_gambar": "https://lh3.googleusercontent.com/aida-public/AB6AXuDZRIPhbMvk_-7tqFMuJ4urLI9CrTKS9gmO4m5-FblYd86SjOX92OHxzJ8e2qB1DYlhXT4BR7POlPJb2cMcc52TG_b41lVkPZlgx4uuEB46CQ65APo48gkeFIprq-CDigQUQEM2X_OMZLex10rBHp3DMOl6BRtc9-JYj99yM5jnPGh6BFQZAMCcLF0JiA_-B3bJH25Uk8G2I61CGcYFcC8Ny8Srkc7ly-5kfzPdwZy3iJ5DWvvEpw-E4pieq9Rkd_yZ_9a1iOvR5sE"
        },
        {
            "nama": "Bercak Daun Cercospora",
            "nama_ilmiah": "Cercospora ipomoeae",
            "deskripsi": "Penyakit jamur ini bermanifestasi sebagai bercak kecil berbentuk bulat hingga tidak beraturan dengan pusat abu-abu atau putih dan tepi coklat tua atau kemerahan. Saat penyakit berkembang, bercak dapat menyatu, menyebabkan hawar daun yang luas. Daun bisa menguning dan rontok sebelum waktunya.",
            "solusi": "Pangkas daun yang terinfeksi. Pastikan tanaman tidak terlalu padat. Gunakan irigasi tetes untuk menghindari membasahi daun. Fungisida seperti mancozeb atau semprotan berbahan dasar tembaga bisa efektif jika diterapkan sejak dini. Jaga kebersihan lahan.",
            "url_gambar": "https://lh3.googleusercontent.com/aida-public/AB6AXuD-zbTawTvvkamw30jzSlNm4XGRTmij1u_WzQg-AgYHjHkyuQZ9PlHDGOKWu7bKcMM24bTCMPAdJaaCFaLdqFBnX9RbqWDKu3JNNJZhS8w41eZnuW5eJ-4rV2HoOCVdEMAGuMSNagdSzki73rxP10bIeR0xVDD6EA0EAZWBeF-O4zXFRZ38p66iPN9BIXwDagyVfeXO7dsdrOc8fLMQjOJBB6sNN0tTChd5vCWlUlb_ge-PfXDv7HboNwhasSHiwBJW_Fmits0jcjo"
        },
        {
            "nama": "Virus Mosaik Kangkung",
            "nama_ilmiah": "Water spinach mosaic virus",
            "deskripsi": "Tanaman yang terinfeksi menunjukkan pola belang hijau muda dan tua (mosaik) pada daun. Daun mungkin terdistorsi, berkerut, atau lebih kecil dari biasanya. Pertumbuhan sering terhambat.",
            "solusi": "Tidak ada obat untuk penyakit virus. Cabut dan musnahkan tanaman yang terinfeksi untuk mencegah penyebaran. Kendalikan vektor kutu daun menggunakan sabun insektisida atau minyak mimba. Gunakan bahan tanam bebas virus.",
            "url_gambar": "https://lh3.googleusercontent.com/aida-public/AB6AXuBpyhyYdwHCmB4AFEt-s7jNebhI5-zpbzvM8xaMfW6sQWkIoxqHafCgYSNLh8jS9q5O40IqUQgKwtAUjkUaXHwwlum-QBR4kI_vrA1hQkEdCRo3YFz09wKxFQ24zUaEilVCq1Limtbp_TyredycWbHk0fS6lRoxZhVKYaiW-ueQNNASDvp7D6YSKK3L9vV9bakNVYMEQlmUK3g-dKyA5CmdlAsetEVdSFn3fiTvVcqil4o41Ajva7AIKEo81Ue1dmIk7VPb60AEHuQ"
        },
        {
            "nama": "Layu Fusarium",
            "nama_ilmiah": "Fusarium oxysporum",
            "deskripsi": "Jamur tular tanah ini menyebabkan daun bagian bawah menguning, seringkali pada satu sisi tanaman. Jaringan pembuluh di batang berubah menjadi coklat. Tanaman layu pada siang hari dan mungkin pulih pada malam hari, akhirnya mati.",
            "solusi": "Gunakan varietas tahan jika tersedia. Perbaiki drainase tanah. Solarisaasi tanah sebelum tanam. Buang tanaman yang terinfeksi dan tanah di sekitarnya. Hindari pemupukan nitrogen berlebihan.",
            "url_gambar": "https://example.com/fusarium.jpg"
        },
        {
            "nama": "Busuk Akar Pythium",
            "nama_ilmiah": "Pythium spp.",
            "deskripsi": "Akar menjadi coklat, lembek, dan kerdil. Tanaman tampak kerdil dan mungkin layu meskipun air cukup. Batang bagian bawah mungkin menjadi lunak dan gelap (damping-off pada bibit).",
            "solusi": "Pastikan drainase tanah sangat baik. Hindari penyiraman berlebihan. Gunakan media tanam steril untuk bibit. Gunakan fungisida khusus untuk Pythium (misalnya metalaksil) jika perlu.",
            "url_gambar": "https://example.com/pythium.jpg"
        },
        {
            "nama": "Busuk Batang Rhizoctonia",
            "nama_ilmiah": "Rhizoctonia solani",
            "deskripsi": "Lesi cekung berwarna coklat kemerahan muncul pada batang di dekat garis tanah. Batang bisa tercekik dan tanaman bisa roboh. Daun mungkin menunjukkan bercak coklat tidak beraturan.",
            "solusi": "Tanam di tanah yang drainasenya baik. Hindari penanaman terlalu dalam. Buang sisa tanaman yang terinfeksi. Gunakan fungisida yang sesuai. Rotasi tanaman.",
            "url_gambar": "https://example.com/rhizoctonia.jpg"
        },
        {
            "nama": "Bercak Daun Alternaria",
            "nama_ilmiah": "Alternaria spp.",
            "deskripsi": "Bercak berbentuk target dengan cincin konsentris terbentuk pada daun. Bercak sering berwarna coklat atau hitam. Daun bisa menguning dan rontok.",
            "solusi": "Buang daun yang terinfeksi. Gunakan fungisida berbahan dasar tembaga. Hindari irigasi overhead. Jaga jarak tanam yang tepat.",
            "url_gambar": "https://example.com/alternaria.jpg"
        },
        {
            "nama": "Bercak Daun Bakteri",
            "nama_ilmiah": "Pseudomonas / Xanthomonas",
            "deskripsi": "Bercak kecil basah muncul pada daun, sering dikelilingi oleh halo kuning. Bercak berubah menjadi coklat atau hitam dan bisa rontok, meninggalkan lubang.",
            "solusi": "Buang bagian tanaman yang terinfeksi. Hindari penyiraman overhead. Gunakan bakterisida berbahan dasar tembaga. Desinfeksi alat.",
            "url_gambar": "https://example.com/bacterial_spot.jpg"
        },
        {
            "nama": "Embun Tepung (Powdery Mildew)",
            "nama_ilmiah": "Erysiphe spp.",
            "deskripsi": "Pertumbuhan jamur putih seperti bubuk muncul di permukaan atas daun. Daun bisa mengeriting atau terdistorsi.",
            "solusi": "Gunakan belerang atau minyak mimba. Tingkatkan sirkulasi udara. Buang bagian yang terinfeksi parah.",
            "url_gambar": "https://example.com/powdery_mildew.jpg"
        },
        {
            "nama": "Embun Bulu (Downy Mildew)",
            "nama_ilmiah": "Peronospora spp.",
            "deskripsi": "Bercak kekuningan pada permukaan atas daun dengan pertumbuhan berbulu halus keabu-abuan/ungu di bagian bawah. Daun bisa berubah coklat dan mati.",
            "solusi": "Kurangi kelembaban. Gunakan fungisida seperti tembaga atau mancozeb. Buang sisa tanaman yang terinfeksi.",
            "url_gambar": "https://example.com/downy_mildew.jpg"
        },
        {
            "nama": "Antraknosa",
            "nama_ilmiah": "Colletotrichum spp.",
            "deskripsi": "Lesi cekung gelap pada batang dan daun. Massa spora merah muda mungkin muncul dalam kondisi basah.",
            "solusi": "Buang bagian yang terinfeksi. Gunakan klorotalonil atau fungisida tembaga. Pastikan benih bebas penyakit.",
            "url_gambar": "https://example.com/anthracnose.jpg"
        },
        {
            "nama": "Serangan Kutu Daun (Aphids)",
            "nama_ilmiah": "Aphidoidea",
            "deskripsi": "Serangga kecil bertubuh lunak berkumpul di pertumbuhan baru dan bagian bawah daun. Daun mengeriting, menguning, dan terdistorsi. Embun madu lengket mungkin ada.",
            "solusi": "Semprot dengan air. Gunakan sabun insektisida atau minyak mimba. Perkenalkan predator alami seperti kepik.",
            "url_gambar": "https://example.com/aphids.jpg"
        },
        {
            "nama": "Serangan Tungau Laba-laba",
            "nama_ilmiah": "Tetranychidae",
            "deskripsi": "Bintik-bintik kuning atau putih kecil (stippling) pada daun. Jaring halus mungkin terlihat. Daun berubah menjadi perunggu atau kuning.",
            "solusi": "Tingkatkan kelembaban. Semprot dengan air. Gunakan akarisida atau minyak mimba.",
            "url_gambar": "https://example.com/spider_mites.jpg"
        },
        {
            "nama": "Pengorok Daun (Leaf Miner)",
            "nama_ilmiah": "Liriomyza spp.",
            "deskripsi": "Terowongan putih berkelok-kelok (mines) terlihat di dalam jaringan daun. Larva makan di antara permukaan daun.",
            "solusi": "Buang daun yang ada terowongannya. Gunakan perangkap lengket kuning untuk dewasa. Gunakan minyak mimba.",
            "url_gambar": "https://example.com/leaf_miner.jpg"
        },
        {
            "nama": "Kekurangan Nitrogen",
            "nama_ilmiah": "Nutrient Deficiency",
            "deskripsi": "Daun tua menguning secara umum (klorosis). Pertumbuhan tanaman lambat dan kerdil.",
            "solusi": "Berikan pupuk kaya nitrogen (misalnya urea, emulsi ikan). Tambahkan kompos ke tanah.",
            "url_gambar": "https://example.com/nitrogen_deficiency.jpg"
        }
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
        {"kode": "G18", "deskripsi": "Lesi cekung gelap pada batang/daun"},
        {"kode": "G19", "deskripsi": "Serangga kecil berkumpul di pucuk/bawah daun"},
        {"kode": "G20", "deskripsi": "Bintik-bintik kuning/putih halus pada daun"},
        {"kode": "G21", "deskripsi": "Jaring halus pada tanaman"},
        {"kode": "G22", "deskripsi": "Terowongan putih berkelok-kelok di dalam daun"},
        {"kode": "G23", "deskripsi": "Daun tua menguning secara menyeluruh"},
        {"kode": "G24", "deskripsi": "Daun berlubang (shot-holes)"},
        {"kode": "G25", "deskripsi": "Massa spora merah muda terlihat"}
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

        # Anthracnose
        ("Antraknosa", "G18", 0.8),
        ("Antraknosa", "G25", 0.7),
        ("Antraknosa", "G07", 0.4),

        # Aphids
        ("Serangan Kutu Daun (Aphids)", "G19", 0.9),
        ("Serangan Kutu Daun (Aphids)", "G03", 0.7),
        ("Serangan Kutu Daun (Aphids)", "G06", 0.3),

        # Spider Mites
        ("Serangan Tungau Laba-laba", "G20", 0.9),
        ("Serangan Tungau Laba-laba", "G21", 0.8),
        ("Serangan Tungau Laba-laba", "G08", 0.4),

        # Leaf Miner
        ("Pengorok Daun (Leaf Miner)", "G22", 0.95),

        # Nitrogen Deficiency
        ("Kekurangan Nitrogen", "G23", 0.9),
        ("Kekurangan Nitrogen", "G07", 0.5),
        ("Kekurangan Nitrogen", "G08", 0.8),
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
