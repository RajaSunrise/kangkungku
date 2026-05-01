from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas

def dapatkan_semua_penyakit(db: Session, lewati: int = 0, batas: int = 100):
    return db.query(models.Penyakit).offset(lewati).limit(batas).all()

def dapatkan_penyakit(db: Session, penyakit_id: int):
    return db.query(models.Penyakit).filter(models.Penyakit.id == penyakit_id).first()

def dapatkan_semua_gejala(db: Session, lewati: int = 0, batas: int = 100):
    return db.query(models.Gejala).offset(lewati).limit(batas).all()

def dapatkan_semua_aturan(db: Session):
    return db.query(models.Aturan).all()

def buat_penyakit(db: Session, penyakit: schemas.PenyakitBase):
    db_penyakit = models.Penyakit(**penyakit.model_dump())
    db.add(db_penyakit)
    db.commit()
    db.refresh(db_penyakit)
    return db_penyakit

def buat_gejala(db: Session, gejala: schemas.GejalaBase):
    db_gejala = models.Gejala(**gejala.model_dump())
    db.add(db_gejala)
    db.commit()
    db.refresh(db_gejala)
    return db_gejala

def buat_aturan(db: Session, penyakit_id: int, gejala_id: int, pakar_cf: float):
    db_aturan = models.Aturan(penyakit_id=penyakit_id, gejala_id=gejala_id, pakar_cf=pakar_cf)
    db.add(db_aturan)
    db.commit()
    db.refresh(db_aturan)
    return db_aturan

def update_penyakit(db: Session, penyakit_id: int, penyakit: schemas.PenyakitBase):
    db_penyakit = db.query(models.Penyakit).filter(models.Penyakit.id == penyakit_id).first()
    if db_penyakit:
        for key, value in penyakit.model_dump(exclude_unset=True).items():
            setattr(db_penyakit, key, value)
        db.commit()
        db.refresh(db_penyakit)
    return db_penyakit

def delete_penyakit(db: Session, penyakit_id: int):
    db_penyakit = db.query(models.Penyakit).filter(models.Penyakit.id == penyakit_id).first()
    if db_penyakit:
        db.delete(db_penyakit)
        db.commit()
    return db_penyakit

def update_gejala(db: Session, gejala_id: int, gejala: schemas.GejalaBase):
    db_gejala = db.query(models.Gejala).filter(models.Gejala.id == gejala_id).first()
    if db_gejala:
        for key, value in gejala.model_dump(exclude_unset=True).items():
            setattr(db_gejala, key, value)
        db.commit()
        db.refresh(db_gejala)
    return db_gejala

def delete_gejala(db: Session, gejala_id: int):
    db_gejala = db.query(models.Gejala).filter(models.Gejala.id == gejala_id).first()
    if db_gejala:
        db.delete(db_gejala)
        db.commit()
    return db_gejala

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def simpan_history(db: Session, user_id: Optional[int], penyakit_id: int, cf: float, persentase: float, gejala_input: str):
    from datetime import datetime
    db_history = models.DiagnosaHistory(
        user_id=user_id,
        penyakit_id=penyakit_id,
        faktor_kepastian=cf,
        persentase=persentase,
        gejala_input=gejala_input,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

def dapatkan_history_user(db: Session, user_id: int):
    return db.query(models.DiagnosaHistory).filter(models.DiagnosaHistory.user_id == user_id).order_by(models.DiagnosaHistory.id.desc()).all()

def dapatkan_statistik(db: Session):
    total_users = db.query(models.User).count()
    total_diagnosa = db.query(models.DiagnosaHistory).count()
    total_penyakit = db.query(models.Penyakit).count()
    total_gejala = db.query(models.Gejala).count()
    history_terbaru = db.query(models.DiagnosaHistory).order_by(models.DiagnosaHistory.id.desc()).limit(10).all()
    
    return {
        "total_users": total_users,
        "total_diagnosa": total_diagnosa,
        "total_penyakit": total_penyakit,
        "total_gejala": total_gejala,
        "history_terbaru": history_terbaru
    }

# ---- User CRUD (Admin) ----

def dapatkan_semua_users(db: Session, lewati: int = 0, batas: int = 100):
    return db.query(models.User).offset(lewati).limit(batas).all()

def dapatkan_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate, hashed_password: str = None):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        update_data = user_data.model_dump(exclude_unset=True, exclude={"password"})
        for key, value in update_data.items():
            if value is not None:
                setattr(db_user, key, value)
        if hashed_password:
            db_user.hashed_password = hashed_password
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        # Also delete related diagnosis history
        db.query(models.DiagnosaHistory).filter(models.DiagnosaHistory.user_id == user_id).delete()
        db.delete(db_user)
        db.commit()
    return db_user

