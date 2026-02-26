from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database
from ..security import get_current_admin

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
