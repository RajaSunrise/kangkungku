from sqlalchemy.orm import Session
from . import model, skema

def dapatkan_semua_penyakit(db: Session, lewati: int = 0, batas: int = 100):
    return db.query(model.Penyakit).offset(lewati).limit(batas).all()

def dapatkan_penyakit(db: Session, penyakit_id: int):
    return db.query(model.Penyakit).filter(model.Penyakit.id == penyakit_id).first()

def dapatkan_semua_gejala(db: Session, lewati: int = 0, batas: int = 100):
    return db.query(model.Gejala).offset(lewati).limit(batas).all()

def dapatkan_semua_aturan(db: Session):
    return db.query(model.Aturan).all()

def buat_penyakit(db: Session, penyakit: skema.PenyakitBase):
    db_penyakit = model.Penyakit(**penyakit.model_dump())
    db.add(db_penyakit)
    db.commit()
    db.refresh(db_penyakit)
    return db_penyakit

def buat_gejala(db: Session, gejala: skema.GejalaBase):
    db_gejala = model.Gejala(**gejala.model_dump())
    db.add(db_gejala)
    db.commit()
    db.refresh(db_gejala)
    return db_gejala

def buat_aturan(db: Session, penyakit_id: int, gejala_id: int, pakar_cf: float):
    db_aturan = model.Aturan(penyakit_id=penyakit_id, gejala_id=gejala_id, pakar_cf=pakar_cf)
    db.add(db_aturan)
    db.commit()
    db.refresh(db_aturan)
    return db_aturan
