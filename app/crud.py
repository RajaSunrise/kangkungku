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
