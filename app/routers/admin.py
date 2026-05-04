from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database
from ..security import get_current_admin, get_password_hash

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(get_current_admin)])

# Diseases
@router.post("/penyakit", response_model=schemas.Penyakit)
def create_penyakit(penyakit: schemas.PenyakitBase, db: Session = Depends(database.get_db)):
    return crud.buat_penyakit(db=db, penyakit=penyakit)

@router.put("/penyakit/{penyakit_id}", response_model=schemas.Penyakit)
def update_penyakit(penyakit_id: int, penyakit: schemas.PenyakitBase, db: Session = Depends(database.get_db)):
    db_penyakit = crud.update_penyakit(db, penyakit_id=penyakit_id, penyakit=penyakit)
    if db_penyakit is None:
        raise HTTPException(status_code=404, detail="Penyakit not found")
    return db_penyakit

@router.delete("/penyakit/{penyakit_id}", response_model=schemas.Penyakit)
def delete_penyakit(penyakit_id: int, db: Session = Depends(database.get_db)):
    db_penyakit = crud.delete_penyakit(db, penyakit_id=penyakit_id)
    if db_penyakit is None:
        raise HTTPException(status_code=404, detail="Penyakit not found")
    return db_penyakit

# Symptoms
@router.post("/gejala", response_model=schemas.Gejala)
def create_gejala(gejala: schemas.GejalaBase, db: Session = Depends(database.get_db)):
    return crud.buat_gejala(db=db, gejala=gejala)

@router.put("/gejala/{gejala_id}", response_model=schemas.Gejala)
def update_gejala(gejala_id: int, gejala: schemas.GejalaBase, db: Session = Depends(database.get_db)):
    db_gejala = crud.update_gejala(db, gejala_id=gejala_id, gejala=gejala)
    if db_gejala is None:
        raise HTTPException(status_code=404, detail="Gejala not found")
    return db_gejala

@router.delete("/gejala/{gejala_id}", response_model=schemas.Gejala)
def delete_gejala(gejala_id: int, db: Session = Depends(database.get_db)):
    db_gejala = crud.delete_gejala(db, gejala_id=gejala_id)
    if db_gejala is None:
        raise HTTPException(status_code=404, detail="Gejala not found")
    return db_gejala

# Rules (Aturan)
@router.get("/aturan", response_model=List[schemas.AturanRead])
def get_all_aturan(db: Session = Depends(database.get_db)):
    aturan_list = crud.dapatkan_semua_aturan(db)
    return aturan_list

@router.get("/aturan/{aturan_id}", response_model=schemas.AturanRead)
def get_aturan(aturan_id: int, db: Session = Depends(database.get_db)):
    db_aturan = crud.dapatkan_aturan(db, aturan_id=aturan_id)
    if db_aturan is None:
        raise HTTPException(status_code=404, detail="Aturan tidak ditemukan")
    return db_aturan

@router.post("/aturan", response_model=schemas.AturanRead)
def create_aturan(aturan: schemas.AturanBase, db: Session = Depends(database.get_db)):
    # Validate penyakit and gejala exist
    penyakit = crud.dapatkan_penyakit(db, penyakit_id=aturan.penyakit_id)
    if not penyakit:
        raise HTTPException(status_code=404, detail="Penyakit tidak ditemukan")
    gejala = db.query(models.Gejala).filter(models.Gejala.id == aturan.gejala_id).first()
    if not gejala:
        raise HTTPException(status_code=404, detail="Gejala tidak ditemukan")
    # Check for duplicate rule
    existing = db.query(models.Aturan).filter(
        models.Aturan.penyakit_id == aturan.penyakit_id,
        models.Aturan.gejala_id == aturan.gejala_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Aturan untuk kombinasi penyakit dan gejala ini sudah ada")
    return crud.buat_aturan(db=db, penyakit_id=aturan.penyakit_id, gejala_id=aturan.gejala_id, pakar_cf=aturan.pakar_cf)

@router.put("/aturan/{aturan_id}", response_model=schemas.AturanRead)
def update_aturan(aturan_id: int, aturan: schemas.AturanBase, db: Session = Depends(database.get_db)):
    # Validate penyakit and gejala exist
    penyakit = crud.dapatkan_penyakit(db, penyakit_id=aturan.penyakit_id)
    if not penyakit:
        raise HTTPException(status_code=404, detail="Penyakit tidak ditemukan")
    gejala = db.query(models.Gejala).filter(models.Gejala.id == aturan.gejala_id).first()
    if not gejala:
        raise HTTPException(status_code=404, detail="Gejala tidak ditemukan")
    # Check for duplicate rule (excluding current)
    existing = db.query(models.Aturan).filter(
        models.Aturan.penyakit_id == aturan.penyakit_id,
        models.Aturan.gejala_id == aturan.gejala_id,
        models.Aturan.id != aturan_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Aturan untuk kombinasi penyakit dan gejala ini sudah ada")
    db_aturan = crud.update_aturan(db, aturan_id=aturan_id, penyakit_id=aturan.penyakit_id, gejala_id=aturan.gejala_id, pakar_cf=aturan.pakar_cf)
    if db_aturan is None:
        raise HTTPException(status_code=404, detail="Aturan tidak ditemukan")
    return db_aturan

@router.delete("/aturan/{aturan_id}", response_model=schemas.AturanRead)
def delete_aturan(aturan_id: int, db: Session = Depends(database.get_db)):
    db_aturan = crud.delete_aturan(db, aturan_id=aturan_id)
    if db_aturan is None:
        raise HTTPException(status_code=404, detail="Aturan tidak ditemukan")
    return db_aturan

# Stats
@router.get("/stats", response_model=schemas.DashboardStats)
def get_stats(db: Session = Depends(database.get_db)):
    return crud.dapatkan_statistik(db)

# ---- Users Management ----

@router.get("/users", response_model=List[schemas.UserRead])
def get_all_users(lewati: int = 0, batas: int = 100, db: Session = Depends(database.get_db)):
    return crud.dapatkan_semua_users(db, lewati=lewati, batas=batas)

@router.get("/users/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.dapatkan_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return db_user

@router.post("/users", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if username already exists
    existing = crud.get_user_by_username(db, username=user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username sudah digunakan")
    # Check if email already exists
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email sudah digunakan")
    hashed_password = get_password_hash(user.password)
    return crud.create_user(db=db, user=user, hashed_password=hashed_password)

@router.put("/users/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, user_data: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = crud.dapatkan_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    
    # Check username uniqueness if changed
    if user_data.username and user_data.username != db_user.username:
        existing = crud.get_user_by_username(db, username=user_data.username)
        if existing:
            raise HTTPException(status_code=400, detail="Username sudah digunakan")
    
    # Check email uniqueness if changed
    if user_data.email and user_data.email != db_user.email:
        existing_email = db.query(models.User).filter(models.User.email == user_data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email sudah digunakan")
    
    hashed_pw = None
    if user_data.password:
        hashed_pw = get_password_hash(user_data.password)
    
    return crud.update_user(db=db, user_id=user_id, user_data=user_data, hashed_password=hashed_pw)

@router.delete("/users/{user_id}", response_model=schemas.UserRead)
def delete_user(user_id: int, db: Session = Depends(database.get_db), current_admin: models.User = Depends(get_current_admin)):
    if current_admin.id == user_id:
        raise HTTPException(status_code=400, detail="Tidak bisa menghapus akun sendiri")
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return db_user
