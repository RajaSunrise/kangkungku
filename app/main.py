from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas, database, expert_system

# Buat tabel
models.Base.metadata.create_all(bind=database.engine)

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
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/gejala", response_model=List[schemas.Gejala])
def baca_gejala(lewati: int = 0, batas: int = 100, db: Session = Depends(dapatkan_db)):
    return crud.dapatkan_semua_gejala(db, lewati=lewati, batas=batas)

@app.post("/api/diagnosa", response_model=List[schemas.HasilDiagnosa])
def diagnosa(permintaan: schemas.PermintaanDiagnosa, db: Session = Depends(dapatkan_db)):
    # Dapatkan semua aturan dari DB
    semua_aturan = crud.dapatkan_semua_aturan(db)

    # Hitung CF
    hasil_diagnosa = expert_system.hitung_diagnosa(permintaan.gejala, semua_aturan)

    # Urutkan berdasarkan CF menurun
    hasil_terurut = sorted(hasil_diagnosa.items(), key=lambda item: item[1], reverse=True)

    respon = []
    for penyakit_id, cf in hasil_terurut:
        penyakit = crud.dapatkan_penyakit(db, penyakit_id=penyakit_id)
        if penyakit:
            respon.append(schemas.HasilDiagnosa(
                penyakit=penyakit,
                faktor_kepastian=cf,
                persentase=round(cf * 100, 2)
            ))

    return respon

@app.get("/api/penyakit", response_model=List[schemas.Penyakit])
def baca_semua_penyakit(lewati: int = 0, batas: int = 100, db: Session = Depends(dapatkan_db)):
    return crud.dapatkan_semua_penyakit(db, lewati=lewati, batas=batas)

@app.get("/api/penyakit/{penyakit_id}", response_model=schemas.Penyakit)
def baca_penyakit(penyakit_id: int, db: Session = Depends(dapatkan_db)):
    db_penyakit = crud.dapatkan_penyakit(db, penyakit_id=penyakit_id)
    if db_penyakit is None:
        raise HTTPException(status_code=404, detail="Penyakit tidak ditemukan")
    return db_penyakit

# Mount static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")
