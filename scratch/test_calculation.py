import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Aturan, Penyakit
from app.schemas import GejalaPengguna
from app.expert_system import hitung_diagnosa
import os
from dotenv import load_dotenv

load_dotenv()

# Setup test DB connection
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("DATABASE_URL not found in environment!")
    sys.exit(1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

try:
    # Symptoms 1, 2, 3 selected by user with confidence 1.0
    user_symptoms = [
        GejalaPengguna(gejala_id=1, keyakinan=1.0), # G001
        GejalaPengguna(gejala_id=2, keyakinan=1.0), # G002
        GejalaPengguna(gejala_id=3, keyakinan=1.0), # G003
    ]

    semua_aturan = db.query(Aturan).all()
    results = hitung_diagnosa(user_symptoms, semua_aturan)

    print("\n--- HASIL DIAGNOSA GEJALA 1, 2, dan 3 ---")
    for penyakit_id, cf in sorted(results.items(), key=lambda x: x[1], reverse=True):
        penyakit = db.query(Penyakit).filter(Penyakit.id == penyakit_id).first()
        print(f"Penyakit: {penyakit.nama} (ID: {penyakit_id}) | Persentase: {cf * 100:.2f}%")
finally:
    db.close()
