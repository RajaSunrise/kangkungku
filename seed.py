from app.database import SessionLocal, engine
from app import models

def seed():
    db = SessionLocal()

    # Create tables
    models.Base.metadata.create_all(bind=engine)

    # Clear existing data
    db.query(models.Rule).delete()
    db.query(models.Symptom).delete()
    db.query(models.Disease).delete()
    db.commit()

    print("Existing data cleared.")

    # Diseases (15)
    diseases_data = [
        {
            "name": "White Rust (Karat Putih)",
            "scientific_name": "Albugo ipomoeae-panduratae",
            "description": "White rust is a fungal disease that causes white, raised pustules on the undersides of leaves. These pustules eventually rupture, releasing white powdery spores. The upper leaf surface may show yellow spots corresponding to the pustules below. Severe infection can cause leaf distortion, stunted growth, and defoliation.",
            "solution": "Remove and destroy infected leaves immediately. Improve air circulation by spacing plants properly. Avoid overhead watering to keep foliage dry. Apply fungicides containing copper or chlorothalonil if the infection is severe. Crop rotation with non-host plants is recommended.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDZRIPhbMvk_-7tqFMuJ4urLI9CrTKS9gmO4m5-FblYd86SjOX92OHxzJ8e2qB1DYlhXT4BR7POlPJb2cMcc52TG_b41lVkPZlgx4uuEB46CQ65APo48gkeFIprq-CDigQUQEM2X_OMZLex10rBHp3DMOl6BRtc9-JYj99yM5jnPGh6BFQZAMCcLF0JiA_-B3bJH25Uk8G2I61CGcYFcC8Ny8Srkc7ly-5kfzPdwZy3iJ5DWvvEpw-E4pieq9Rkd_yZ_9a1iOvR5sE"
        },
        {
            "name": "Cercospora Leaf Spot (Bercak Daun Cercospora)",
            "scientific_name": "Cercospora ipomoeae",
            "description": "This fungal disease manifests as small, circular to irregular spots with gray or white centers and dark brown or reddish borders. As the disease progresses, spots may coalesce, causing extensive leaf blight. Leaves may yellow and drop prematurely.",
            "solution": "Prune infected leaves. Ensure plants are not overcrowded. Use drip irrigation to avoid wetting leaves. Fungicides such as mancozeb or copper-based sprays can be effective if applied early. Maintain field hygiene.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuD-zbTawTvvkamw30jzSlNm4XGRTmij1u_WzQg-AgYHjHkyuQZ9PlHDGOKWu7bKcMM24bTCMPAdJaaCFaLdqFBnX9RbqWDKu3JNNJZhS8w41eZnuW5eJ-4rV2HoOCVdEMAGuMSNagdSzki73rxP10bIeR0xVDD6EA0EAZWBeF-O4zXFRZ38p66iPN9BIXwDagyVfeXO7dsdrOc8fLMQjOJBB6sNN0tTChd5vCWlUlb_ge-PfXDv7HboNwhasSHiwBJW_Fmits0jcjo"
        },
        {
            "name": "Water Spinach Mosaic Virus (Virus Mosaik)",
            "scientific_name": "Water spinach mosaic virus",
            "description": "Infected plants show mottled light and dark green patterns (mosaic) on leaves. Leaves may be distorted, crinkled, or smaller than normal. Growth is often stunted.",
            "solution": "There is no cure for viral diseases. Remove and destroy infected plants to prevent spread. Control aphid vectors using insecticidal soap or neem oil. Use virus-free planting material.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBpyhyYdwHCmB4AFEt-s7jNebhI5-zpbzvM8xaMfW6sQWkIoxqHafCgYSNLh8jS9q5O40IqUQgKwtAUjkUaXHwwlum-QBR4kI_vrA1hQkEdCRo3YFz09wKxFQ24zUaEilVCq1Limtbp_TyredycWbHk0fS6lRoxZhVKYaiW-ueQNNASDvp7D6YSKK3L9vV9bakNVYMEQlmUK3g-dKyA5CmdlAsetEVdSFn3fiTvVcqil4o41Ajva7AIKEo81Ue1dmIk7VPb60AEHuQ"
        },
        {
            "name": "Fusarium Wilt (Layu Fusarium)",
            "scientific_name": "Fusarium oxysporum",
            "description": "This soil-borne fungus causes yellowing of lower leaves, often on one side of the plant. The vascular tissue in the stem turns brown. The plant wilts during the day and may recover at night, eventually dying.",
            "solution": "Use resistant varieties if available. Improve soil drainage. Solarize soil before planting. Remove infected plants and surrounding soil. Avoid excessive nitrogen fertilization.",
            "image_url": "https://example.com/fusarium.jpg"
        },
        {
            "name": "Pythium Root Rot (Busuk Akar Pythium)",
            "scientific_name": "Pythium spp.",
            "description": "Roots become brown, mushy, and stunted. Plants appear stunted and may wilt despite adequate water. Lower stems may become soft and dark (damping-off in seedlings).",
            "solution": "Ensure excellent soil drainage. Avoid overwatering. Use sterile potting mix for seedlings. Apply fungicides specifically for Pythium (e.g., metalaxyl) if necessary.",
            "image_url": "https://example.com/pythium.jpg"
        },
        {
            "name": "Rhizoctonia Stem Rot (Busuk Batang Rhizoctonia)",
            "scientific_name": "Rhizoctonia solani",
            "description": "Reddish-brown sunken lesions appear on stems near the soil line. Stems may girdle and plant may collapse. Leaves may show irregular brown spots.",
            "solution": "Plant in well-draining soil. Avoid deep planting. Remove infected plant debris. Apply appropriate fungicides. rotate crops.",
            "image_url": "https://example.com/rhizoctonia.jpg"
        },
        {
            "name": "Alternaria Leaf Spot (Bercak Daun Alternaria)",
            "scientific_name": "Alternaria spp.",
            "description": "Target-shaped spots with concentric rings form on leaves. Spots are often brown or black. Leaves may yellow and drop.",
            "solution": "Remove infected leaves. Apply copper-based fungicides. avoid overhead irrigation. maintain proper plant spacing.",
            "image_url": "https://example.com/alternaria.jpg"
        },
        {
            "name": "Bacterial Leaf Spot (Bercak Daun Bakteri)",
            "scientific_name": "Pseudomonas / Xanthomonas",
            "description": "Small, water-soaked spots appear on leaves, often surrounded by a yellow halo. Spots turn brown or black and may fall out, leaving shot-holes.",
            "solution": "Remove infected plant parts. Avoid overhead watering. Apply copper-based bactericides. Disinfect tools.",
            "image_url": "https://example.com/bacterial_spot.jpg"
        },
        {
            "name": "Powdery Mildew (Embun Tepung)",
            "scientific_name": "Erysiphe spp.",
            "description": "White, powdery fungal growth appears on upper leaf surfaces. Leaves may curl or become distorted.",
            "solution": "Apply sulfur or neem oil. Improve air circulation. Remove severely infected parts.",
            "image_url": "https://example.com/powdery_mildew.jpg"
        },
        {
            "name": "Downy Mildew (Embun Bulu)",
            "scientific_name": "Peronospora spp.",
            "description": "Yellowish patches on upper leaf surface with greyish/purple fuzzy growth on the underside. Leaves may turn brown and die.",
            "solution": "Reduce humidity. Apply fungicides like copper or mancozeb. Remove infected debris.",
            "image_url": "https://example.com/downy_mildew.jpg"
        },
        {
            "name": "Anthracnose (Antraknosa)",
            "scientific_name": "Colletotrichum spp.",
            "description": "Dark, sunken lesions on stems and leaves. Pinkish spore masses may appear in wet conditions.",
            "solution": "Remove infected parts. Apply chlorothalonil or copper fungicides. Ensure seeds are disease-free.",
            "image_url": "https://example.com/anthracnose.jpg"
        },
        {
            "name": "Aphid Infestation (Serangan Kutu Daun)",
            "scientific_name": "Aphidoidea",
            "description": "Small, soft-bodied insects cluster on new growth and undersides of leaves. Leaves curl, yellow, and become distorted. Sticky honeydew may be present.",
            "solution": "Blast off with water. Use insecticidal soap or neem oil. Introduce natural predators like ladybugs.",
            "image_url": "https://example.com/aphids.jpg"
        },
        {
            "name": "Spider Mite Infestation (Tungau Laba-laba)",
            "scientific_name": "Tetranychidae",
            "description": "Tiny yellow or white speckles (stippling) on leaves. Fine webbing may be visible. Leaves turn bronze or yellow.",
            "solution": "Increase humidity. Spray with water. Use miticides or neem oil.",
            "image_url": "https://example.com/spider_mites.jpg"
        },
        {
            "name": "Leaf Miner Damage (Pengorok Daun)",
            "scientific_name": "Liriomyza spp.",
            "description": "White, serpentine tunnels (mines) visible within leaf tissue. Larvae feed between leaf surfaces.",
            "solution": "Remove mined leaves. Use yellow sticky traps for adults. Apply neem oil.",
            "image_url": "https://example.com/leaf_miner.jpg"
        },
        {
            "name": "Nitrogen Deficiency (Kekurangan Nitrogen)",
            "scientific_name": "Nutrient Deficiency",
            "description": "General yellowing of older leaves (chlorosis). Plant growth is slow and stunted.",
            "solution": "Apply nitrogen-rich fertilizer (e.g., urea, fish emulsion). Add compost to soil.",
            "image_url": "https://example.com/nitrogen_deficiency.jpg"
        }
    ]

    # Insert Diseases
    db_diseases = []
    for d_data in diseases_data:
        disease = models.Disease(**d_data)
        db.add(disease)
        db_diseases.append(disease)
    db.commit()

    # Reload diseases to get IDs
    db_diseases = db.query(models.Disease).all()
    d_map = {d.name: d.id for d in db_diseases}

    # Symptoms
    symptoms_data = [
        {"code": "S01", "description": "Bercak putih menonjol pada sisi bawah daun (White raised pustules on underside)"},
        {"code": "S02", "description": "Bercak kuning pada sisi atas daun (Yellow spots on upper leaf surface)"},
        {"code": "S03", "description": "Daun melengkung atau terdistorsi (Distorted or curled leaves)"},
        {"code": "S04", "description": "Bercak bulat dengan pusat abu-abu/putih (Circular spots with gray/white centers)"},
        {"code": "S05", "description": "Bercak dengan tepi coklat tua/merah (Spots with dark brown/red borders)"},
        {"code": "S06", "description": "Pola mosaik hijau terang/gelap (Mottled light/dark green mosaic pattern)"},
        {"code": "S07", "description": "Pertumbuhan kerdil (Stunted growth)"},
        {"code": "S08", "description": "Daun bagian bawah menguning (Lower leaves yellowing)"},
        {"code": "S09", "description": "Layu pada siang hari, pulih malam hari (Wilts during day, recovers at night)"},
        {"code": "S10", "description": "Jaringan pembuluh batang berwarna coklat (Brown vascular tissue in stem)"},
        {"code": "S11", "description": "Akar berwarna coklat dan lembek (Brown, mushy roots)"},
        {"code": "S12", "description": "Batang lunak dan gelap di dekat tanah (Soft, dark stem near soil)"},
        {"code": "S13", "description": "Lesi cekung kemerahan pada batang (Reddish sunken lesions on stem)"},
        {"code": "S14", "description": "Bercak seperti target dengan cincin konsentris (Target-shaped spots)"},
        {"code": "S15", "description": "Bercak basah dikelilingi halo kuning (Water-soaked spots with yellow halo)"},
        {"code": "S16", "description": "Serbuk putih pada permukaan daun (White powdery growth on leaves)"},
        {"code": "S17", "description": "Pertumbuhan berbulu abu-abu/ungu di bawah daun (Grey/purple fuzzy growth on underside)"},
        {"code": "S18", "description": "Lesi cekung gelap pada batang/daun (Dark sunken lesions)"},
        {"code": "S19", "description": "Serangga kecil berkumpul di pucuk/bawah daun (Small insects clustering)"},
        {"code": "S20", "description": "Bintik-bintik kuning/putih halus pada daun (Tiny yellow/white stippling)"},
        {"code": "S21", "description": "Jaring halus pada tanaman (Fine webbing)"},
        {"code": "S22", "description": "Terowongan putih berkelok-kelok di dalam daun (White serpentine tunnels)"},
        {"code": "S23", "description": "Daun tua menguning secara umum (General yellowing of older leaves)"},
        {"code": "S24", "description": "Daun berlubang (Shot-holes)"},
        {"code": "S25", "description": "Massa spora merah muda (Pinkish spore masses)"}
    ]

    # Insert Symptoms
    db_symptoms = []
    for s_data in symptoms_data:
        symptom = models.Symptom(**s_data)
        db.add(symptom)
        db_symptoms.append(symptom)
    db.commit()

    # Reload symptoms
    db_symptoms = db.query(models.Symptom).all()
    s_map = {s.code: s.id for s in db_symptoms}

    # Rules (Disease Name, Symptom Code, Expert CF)
    rules_data = [
        # White Rust
        ("White Rust (Karat Putih)", "S01", 0.9),
        ("White Rust (Karat Putih)", "S02", 0.7),
        ("White Rust (Karat Putih)", "S03", 0.5),

        # Cercospora Leaf Spot
        ("Cercospora Leaf Spot (Bercak Daun Cercospora)", "S04", 0.8),
        ("Cercospora Leaf Spot (Bercak Daun Cercospora)", "S05", 0.8),
        ("Cercospora Leaf Spot (Bercak Daun Cercospora)", "S08", 0.4),

        # Mosaic Virus
        ("Water Spinach Mosaic Virus (Virus Mosaik)", "S06", 0.95),
        ("Water Spinach Mosaic Virus (Virus Mosaik)", "S03", 0.6),
        ("Water Spinach Mosaic Virus (Virus Mosaik)", "S07", 0.7),

        # Fusarium Wilt
        ("Fusarium Wilt (Layu Fusarium)", "S08", 0.6),
        ("Fusarium Wilt (Layu Fusarium)", "S09", 0.9),
        ("Fusarium Wilt (Layu Fusarium)", "S10", 0.8),
        ("Fusarium Wilt (Layu Fusarium)", "S07", 0.5),

        # Pythium Root Rot
        ("Pythium Root Rot (Busuk Akar Pythium)", "S11", 0.9),
        ("Pythium Root Rot (Busuk Akar Pythium)", "S07", 0.6),
        ("Pythium Root Rot (Busuk Akar Pythium)", "S09", 0.5),

        # Rhizoctonia Stem Rot
        ("Rhizoctonia Stem Rot (Busuk Batang Rhizoctonia)", "S12", 0.8),
        ("Rhizoctonia Stem Rot (Busuk Batang Rhizoctonia)", "S13", 0.9),
        ("Rhizoctonia Stem Rot (Busuk Batang Rhizoctonia)", "S09", 0.4),

        # Alternaria Leaf Spot
        ("Alternaria Leaf Spot (Bercak Daun Alternaria)", "S14", 0.9),
        ("Alternaria Leaf Spot (Bercak Daun Alternaria)", "S08", 0.5),

        # Bacterial Leaf Spot
        ("Bacterial Leaf Spot (Bercak Daun Bakteri)", "S15", 0.9),
        ("Bacterial Leaf Spot (Bercak Daun Bakteri)", "S24", 0.7),
        ("Bacterial Leaf Spot (Bercak Daun Bakteri)", "S08", 0.4),

        # Powdery Mildew
        ("Powdery Mildew (Embun Tepung)", "S16", 0.95),
        ("Powdery Mildew (Embun Tepung)", "S03", 0.5),

        # Downy Mildew
        ("Downy Mildew (Embun Bulu)", "S17", 0.9),
        ("Downy Mildew (Embun Bulu)", "S02", 0.6),
        ("Downy Mildew (Embun Bulu)", "S08", 0.5),

        # Anthracnose
        ("Anthracnose (Antraknosa)", "S18", 0.8),
        ("Anthracnose (Antraknosa)", "S25", 0.7),
        ("Anthracnose (Antraknosa)", "S07", 0.4),

        # Aphids
        ("Aphid Infestation (Serangan Kutu Daun)", "S19", 0.9),
        ("Aphid Infestation (Serangan Kutu Daun)", "S03", 0.7),
        ("Aphid Infestation (Serangan Kutu Daun)", "S06", 0.3), # Can cause mosaic-like symptoms

        # Spider Mites
        ("Spider Mite Infestation (Tungau Laba-laba)", "S20", 0.9),
        ("Spider Mite Infestation (Tungau Laba-laba)", "S21", 0.8),
        ("Spider Mite Infestation (Tungau Laba-laba)", "S08", 0.4),

        # Leaf Miner
        ("Leaf Miner Damage (Pengorok Daun)", "S22", 0.95),

        # Nitrogen Deficiency
        ("Nitrogen Deficiency (Kekurangan Nitrogen)", "S23", 0.9),
        ("Nitrogen Deficiency (Kekurangan Nitrogen)", "S07", 0.5),
        ("Nitrogen Deficiency (Kekurangan Nitrogen)", "S08", 0.8),
    ]

    # Insert Rules
    for d_name, s_code, cf in rules_data:
        disease_id = d_map.get(d_name)
        symptom_id = s_map.get(s_code)

        if disease_id and symptom_id:
            rule = models.Rule(disease_id=disease_id, symptom_id=symptom_id, expert_cf=cf)
            db.add(rule)

    db.commit()
    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed()
