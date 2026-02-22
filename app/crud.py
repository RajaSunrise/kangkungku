from sqlalchemy.orm import Session
from . import models, schemas

def get_diseases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disease).offset(skip).limit(limit).all()

def get_disease(db: Session, disease_id: int):
    return db.query(models.Disease).filter(models.Disease.id == disease_id).first()

def get_symptoms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Symptom).offset(skip).limit(limit).all()

def get_rules(db: Session, disease_id: int = None):
    query = db.query(models.Rule)
    if disease_id:
        query = query.filter(models.Rule.disease_id == disease_id)
    return query.all()

def get_all_rules(db: Session):
    return db.query(models.Rule).all()

def create_disease(db: Session, disease: schemas.DiseaseBase):
    db_disease = models.Disease(**disease.model_dump())
    db.add(db_disease)
    db.commit()
    db.refresh(db_disease)
    return db_disease

def create_symptom(db: Session, symptom: schemas.SymptomBase):
    db_symptom = models.Symptom(**symptom.model_dump())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    return db_symptom

def create_rule(db: Session, disease_id: int, symptom_id: int, expert_cf: float):
    db_rule = models.Rule(disease_id=disease_id, symptom_id=symptom_id, expert_cf=expert_cf)
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule
