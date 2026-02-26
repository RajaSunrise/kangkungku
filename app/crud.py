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
