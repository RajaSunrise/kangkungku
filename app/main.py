from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
import json

from . import crud, models, schemas, database, expert_system, security
from .routers import auth, admin

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

app.include_router(auth.router)
app.include_router(admin.router)

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
def diagnosa(permintaan: schemas.PermintaanDiagnosa, db: Session = Depends(dapatkan_db), request: Request = None):
    # Dapatkan user jika ada (opsional)
    user = None
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        try:
            token = auth_header.split(" ")[1]
            user = security.get_current_user(token=token, db=db)
        except:
            pass

    # Dapatkan semua aturan dari DB
    semua_aturan = crud.dapatkan_semua_aturan(db)

    # Hitung CF
    hasil_diagnosa = expert_system.hitung_diagnosa(permintaan.gejala, semua_aturan)

    # Urutkan berdasarkan CF menurun
    hasil_terurut = sorted(hasil_diagnosa.items(), key=lambda item: item[1], reverse=True)

    respon = []
    gejala_ids = [g.gejala_id for g in permintaan.gejala]
    gejala_json = json.dumps(gejala_ids)

    for i, (penyakit_id, cf) in enumerate(hasil_terurut):
        penyakit = crud.dapatkan_penyakit(db, penyakit_id=penyakit_id)
        if penyakit:
            persentase = round(cf * 100, 2)
            respon.append(schemas.HasilDiagnosa(
                penyakit=penyakit,
                faktor_kepastian=cf,
                persentase=persentase
            ))
            
            # Simpan ke history jika ini hasil tertinggi dan user login
            if i == 0 and user:
                crud.simpan_history(
                    db=db,
                    user_id=user.id,
                    penyakit_id=penyakit_id,
                    cf=cf,
                    persentase=persentase,
                    gejala_input=gejala_json
                )
            # Simpan ke history anonim jika tertinggi (untuk statistik admin)
            elif i == 0 and not user:
                crud.simpan_history(
                    db=db,
                    user_id=None,
                    penyakit_id=penyakit_id,
                    cf=cf,
                    persentase=persentase,
                    gejala_input=gejala_json
                )

    return respon

@app.get("/api/history", response_model=List[schemas.DiagnosaHistoryRead])
def baca_history_saya(db: Session = Depends(dapatkan_db), current_user: models.User = Depends(security.get_current_user)):
    return crud.dapatkan_history_user(db, user_id=current_user.id)

@app.get("/api/history/{history_id}", response_model=schemas.DiagnosaHistoryRead)
def baca_detail_history(history_id: int, db: Session = Depends(dapatkan_db), current_user: models.User = Depends(security.get_current_user)):
    history = db.query(models.DiagnosaHistory).filter(models.DiagnosaHistory.id == history_id).first()
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    if history.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return history

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
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/diagnosis.html")
def read_diagnosis(request: Request):
    return templates.TemplateResponse("diagnosis.html", {"request": request})

@app.get("/encyclopedia.html")
def read_encyclopedia(request: Request):
    return templates.TemplateResponse("encyclopedia.html", {"request": request})

@app.get("/calculator.html")
def read_calculator(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.get("/community.html")
def read_community(request: Request):
    return templates.TemplateResponse("community.html", {"request": request})

@app.get("/blog.html")
def read_blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/dashboard.html")
def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/admin.html")
def read_admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/login.html")
def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register.html")
def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/result.html")
def read_result(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})
