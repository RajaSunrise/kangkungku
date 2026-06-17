from app.database import SessionLocal, engine
from app import models
from app.security import get_password_hash

def tebar():
    db = SessionLocal()

    # Create tables
    models.Base.metadata.drop_all(bind=engine)
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
    admin_user = models.User(username="indraaja", hashed_password=admin_password, role="admin", alamat="Jl. Admin No. 1")
    db.add(admin_user)

    # Create User
    user_password = get_password_hash("user1234")
    regular_user = models.User(username="user123", hashed_password=user_password, role="user", alamat="Jl. User No. 2")
    db.add(regular_user)

    db.commit()
    print("User admin dan user biasa dibuat.")

    # Diseases (9)
    data_penyakit = [
        {
            'nama': 'Bekicot',
            'deskripsi': 'Bekicot (Achatina fulica) merupakan hama penting yang menyerang tanaman kangkung dengan memakan daun dan batang muda. Serangan biasanya terjadi secara masif pada malam hari atau kondisi lingkungan yang sangat lembab, meninggalkan lubang-lubang besar yang tidak beraturan serta jejak lendir mengkilap pada permukaan tanaman.',
            'solusi': 'Lakukan pencarian secara manual pada malam hari untuk mengumpulkan dan memusnahkan bekicot secara langsung. Taburkan abu kayu, serbuk gergaji, pasir kasar, atau pecahan cangkang telur di sekeliling bedengan tanaman sebagai penghalang fisik agar bekicot tidak mendekat. Gunakan umpan siput (moluskisida) berbahan aktif metaldehida secara bijaksana dan sesuai dosis anjuran jika serangan sudah melebihi batas kendali.',
            'url_gambar': '/static/img/alternaria.png'
        },
        {
            'nama': 'Ulat Grayak',
            'deskripsi': 'Ulat Grayak (Spodoptera litura) adalah larva serangga yang sangat rakus dan merusak daun kangkung secara berkelompok. Hama ini aktif memakan helaian daun mulai dari tepi hingga menyisakan tulang daunnya saja, terutama di malam hari, sehingga mengganggu proses fotosintesis secara drastis.',
            'solusi': 'Lakukan sanitasi lahan secara rutin dengan membersihkan gulma yang dapat menjadi tempat persembunyian ulat grayak. Kumpulkan kelompok telur dan ulat kecil yang ditemukan pada permukaan bawah daun lalu musnahkan segera. Semprotkan insektisida nabati berbasis minyak mimba atau Beauveria bassiana secara merata di sore hari, atau gunakan insektisida kimia berbahan aktif deltametrin jika populasi hama sangat tinggi.',
            'url_gambar': '/static/img/alternaria.png'
        },
        {
            'nama': 'Kutu Daun',
            'deskripsi': 'Kutu Daun (Aphids) adalah serangga kecil penghisap cairan sel tanaman kangkung, biasanya mengelompok di bagian bawah daun atau pucuk muda. Serangan hama ini menyebabkan helaian daun mengkerut, melengkung, menguning, dan tanaman tumbuh kerdil, serta dapat menularkan penyakit virus lainnya.',
            'solusi': 'Semprot tanaman kangkung menggunakan air bertekanan kuat secara rutin untuk meluruhkan koloni kutu daun dari permukaan daun. Aplikasikan sabun insektisida organik atau minyak mimba secara berkala pada bagian bawah daun yang terserang. Pasang perangkap kartu kuning lengket di sekitar lahan untuk memantau dan meminimalkan populasi kutu daun dewasa.',
            'url_gambar': '/static/img/virus-mosaik.png'
        },
        {
            'nama': 'Ulat Keket',
            'deskripsi': 'Ulat Keket atau ulat tanduk merupakan larva berukuran besar dari ngengat Agrius convolvuli yang memakan daun kangkung dengan sangat cepat. Akibat gigitannya, daun kangkung dapat rusak parah dan bahkan menyisakan batangnya saja dalam beberapa hari jika tidak segera ditangani.',
            'solusi': 'Lakukan pemantauan intensif pada pagi dan sore hari untuk menemukan ulat keket secara manual karena ukurannya yang besar memudahkan pengamatan fisik. Pungut ulat tersebut langsung dari batang kangkung dan musnahkan. Jika serangan meluas, semprot tanaman dengan insektisida hayati berbahan aktif Bacillus thuringiensis yang sangat efektif mengendalikan ulat daun.',
            'url_gambar': '/static/img/alternaria.png'
        },
        {
            'nama': 'Karat Putih',
            'deskripsi': 'Karat Putih adalah penyakit yang disebabkan oleh oomycete Albugo ipomoeae-panduratae. Penyakit ini menyerang daun kangkung dengan memicu bintik kuning di permukaan atas dan pustula putih berkapur di permukaan bawah daun, sehingga menurunkan kualitas panen secara signifikan.',
            'solusi': 'Cabut dan musnahkan daun atau tanaman kangkung yang terinfeksi karat putih untuk memutus siklus penyebaran spora melalui angin. Atur jarak tanam kangkung minimal 15-20 cm untuk menjaga sirkulasi udara di sekitar tajuk daun tetap optimal. Aplikasikan fungisida berbasis sulfur secara berkala atau gunakan fungisida berbahan aktif tembaga oksida sesuai anjuran jika infeksi meluas.',
            'url_gambar': '/static/img/karat-putih.png'
        },
        {
            'nama': 'Bercak Daun',
            'deskripsi': 'Penyakit bercak daun kangkung ditandai dengan munculnya noda atau bercak kecokelatan hingga kehitaman pada permukaan daun. Infeksi jamur ini berkembang sangat pesat pada cuaca hangat dan kelembaban udara yang tinggi, yang mengakibatkan daun layu dan gugur sebelum waktunya.',
            'solusi': 'Pangkas daun yang menunjukkan gejala bercak kecokelatan dan jaga kebersihan area lahan dari serpihan sisa tanaman yang gugur. Hindari penyiraman di sore hari secara langsung pada daun dan lebih baik lakukan penyiraman pada area perakaran di pagi hari. Gunakan fungisida organik berbahan ekstrak bawang putih atau semprotkan fungisida mankozeb sesuai dosis anjuran.',
            'url_gambar': '/static/img/Cercospora.png'
        },
        {
            'nama': 'Bakteri',
            'deskripsi': 'Penyakit bakteri menyerang jaringan vaskular tanaman kangkung, menyebabkan batang membubur lunak, mengeluarkan lendir keruh dari jaringan yang terinfeksi, serta mengeluarkan aroma busuk yang sangat menyengat.',
            'solusi': 'Segera cabut tanaman kangkung yang membusuk beserta tanah perakarannya lalu bakar di luar area budidaya untuk mencegah kontaminasi tanah. Pastikan sistem drainase lahan berjalan dengan baik sehingga tidak terjadi genangan air yang memicu perkembangbiakan bakteri patogen. Gunakan bakterisida berbahan aktif tembaga hidroksida untuk mensterilkan tanaman di sekitarnya.',
            'url_gambar': '/static/img/busuk-akar-pythium.png'
        },
        {
            'nama': 'Virus',
            'deskripsi': 'Penyakit virus mosaik kangkung ditandai dengan pola warna belang hijau tua dan hijau muda yang tidak teratur, daun menguning pekat, keriput, batang mengalami bercak-bercak, serta tanaman tumbuh sangat kerdil.',
            'solusi': 'Eradikasi atau cabut dan bakar seluruh tanaman kangkung yang bergejala mosaik untuk mencegah penyebaran virus ke tanaman sehat lainnya. Kendalikan populasi serangga vektor penular seperti kutu daun dengan menyemprotkan sabun insektisida atau minyak mimba secara berkala. Selalu lakukan sterilisasi peralatan pertanian menggunakan alkohol sebelum digunakan berpindah tanaman.',
            'url_gambar': '/static/img/virus-mosaik.png'
        },
        {
            'nama': 'Alga',
            'deskripsi': 'Penyakit alga merah dipicu oleh organisme Cephaleuros virescens. Penyakit ini memicu bercak karat merah atau kelabu kehijauan pada daun kangkung, disertai dengan pertumbuhan rambut halus cokelat kemerahan di permukaannya.',
            'solusi': 'Lakukan pemangkasan pada daun-daun kangkung yang tua atau bagian tanaman terbawah yang terlalu lembab untuk meminimalkan paparan spora alga. Pastikan lahan terpapar sinar matahari secara penuh dan hindari tingkat kerapatan tanaman yang berlebihan. Lakukan penyemprotan fungisida berbahan aktif tembaga jika tingkat serangan alga merusak sebagian besar dedaunan.',
            'url_gambar': '/static/img/embun-bulu.png'
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

    # Symptoms (24)
    data_gejala = [
        {"kode": "G001", "deskripsi": "Batang dan daun rusak"},
        {"kode": "G002", "deskripsi": "Batang dan daun layu"},
        {"kode": "G003", "deskripsi": "Batang dan daun busuk"},
        {"kode": "G004", "deskripsi": "Daun berlubang"},
        {"kode": "G005", "deskripsi": "Pinggir daun bergerigi"},
        {"kode": "G006", "deskripsi": "Tanaman kerdil"},
        {"kode": "G007", "deskripsi": "Daun melengkung"},
        {"kode": "G008", "deskripsi": "Warna daun hijau muda dengan garis menyilang kuning"},
        {"kode": "G009", "deskripsi": "Muncul bercak putih pada permukaan daun"},
        {"kode": "G010", "deskripsi": "Muncul bercak kecokelatan hingga kehitaman pada permukaan daun"},
        {"kode": "G011", "deskripsi": "Mengeluarkan lendir keruh"},
        {"kode": "G012", "deskripsi": "Berbau busuk"},
        {"kode": "G013", "deskripsi": "Keluar air pada batang"},
        {"kode": "G014", "deskripsi": "Lengket jika disentuh"},
        {"kode": "G015", "deskripsi": "Daun berwarna kuning pekat"},
        {"kode": "G016", "deskripsi": "Batang mengalami bercak-bercak"},
        {"kode": "G017", "deskripsi": "Daun menjadi seperti terbakar"},
        {"kode": "G018", "deskripsi": "Bentuk daun menjadi tidak sempurna"},
        {"kode": "G019", "deskripsi": "Daun layu"},
        {"kode": "G020", "deskripsi": "Bercak berwarna kelabu kehijauan pada daun"},
        {"kode": "G021", "deskripsi": "Pada permukaan tumbuh rambut berwarna cokelat kemerahan"},
        {"kode": "G022", "deskripsi": "Daun dihinggapi lalat"},
        {"kode": "G023", "deskripsi": "Batang dan daun kering"},
        {"kode": "G024", "deskripsi": "Bercak karat merah pada daun"},
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

    # Rules (Disease Name, Symptom Code, Expert CF = 1.0)
    data_aturan = [
        ("Bekicot", "G001", 1.0),
        ("Bekicot", "G002", 1.0),
        ("Bekicot", "G003", 1.0),
        ("Ulat Grayak", "G001", 1.0),
        ("Ulat Grayak", "G004", 1.0),
        ("Ulat Grayak", "G005", 1.0),
        ("Kutu Daun", "G006", 1.0),
        ("Kutu Daun", "G007", 1.0),
        ("Ulat Keket", "G001", 1.0),
        ("Ulat Keket", "G004", 1.0),
        ("Ulat Keket", "G008", 1.0),
        ("Karat Putih", "G001", 1.0),
        ("Karat Putih", "G009", 1.0),
        ("Bercak Daun", "G001", 1.0),
        ("Bercak Daun", "G010", 1.0),
        ("Bakteri", "G011", 1.0),
        ("Bakteri", "G012", 1.0),
        ("Bakteri", "G014", 1.0),
        ("Virus", "G016", 1.0),
        ("Virus", "G017", 1.0),
        ("Virus", "G018", 1.0),
        ("Alga", "G020", 1.0),
        ("Alga", "G021", 1.0),
        ("Alga", "G024", 1.0),
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
