from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import operasi, model, skema, basisdata, sistem_pakar

# Buat tabel
model.Base.metadata.create_all(bind=basisdata.engine)

app = FastAPI(title="KangkungKu API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def dapatkan_db():
    db = basisdata.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/gejala", response_model=List[skema.Gejala])
def baca_gejala(lewati: int = 0, batas: int = 100, db: Session = Depends(dapatkan_db)):
    return operasi.dapatkan_semua_gejala(db, lewati=lewati, batas=batas)

@app.post("/api/diagnosa", response_model=List[skema.HasilDiagnosa])
def diagnosa(permintaan: skema.PermintaanDiagnosa, db: Session = Depends(dapatkan_db)):
    # Dapatkan semua aturan dari DB
    semua_aturan = operasi.dapatkan_semua_aturan(db)

    # Hitung CF
    hasil_diagnosa = sistem_pakar.hitung_diagnosa(permintaan.gejala, semua_aturan)

    # Urutkan berdasarkan CF menurun
    hasil_terurut = sorted(hasil_diagnosa.items(), key=lambda item: item[1], reverse=True)

    respon = []
    for penyakit_id, cf in hasil_terurut:
        penyakit = operasi.dapatkan_penyakit(db, penyakit_id=penyakit_id)
        if penyakit:
            respon.append(skema.HasilDiagnosa(
                penyakit=penyakit,
                faktor_kepastian=cf,
                persentase=round(cf * 100, 2)
            ))

    return respon

@app.get("/api/penyakit", response_model=List[skema.Penyakit])
def baca_semua_penyakit(lewati: int = 0, batas: int = 100, db: Session = Depends(dapatkan_db)):
    return operasi.dapatkan_semua_penyakit(db, lewati=lewati, batas=batas)

@app.get("/api/penyakit/{penyakit_id}", response_model=skema.Penyakit)
def baca_penyakit(penyakit_id: int, db: Session = Depends(dapatkan_db)):
    db_penyakit = operasi.dapatkan_penyakit(db, penyakit_id=penyakit_id)
    if db_penyakit is None:
        raise HTTPException(status_code=404, detail="Penyakit tidak ditemukan")
    return db_penyakit

# Mount static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")
