from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas, database, expert_system

# Create tables
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
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/symptoms", response_model=List[schemas.Symptom])
def read_symptoms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_symptoms(db, skip=skip, limit=limit)

@app.post("/api/diagnose", response_model=List[schemas.DiagnosisResult])
def diagnose(request: schemas.DiagnosisRequest, db: Session = Depends(get_db)):
    # Get all rules from DB
    all_rules = crud.get_all_rules(db)

    # Calculate CF
    diagnosis_results = expert_system.calculate_diagnosis(request.symptoms, all_rules)

    # Sort by CF descending
    sorted_results = sorted(diagnosis_results.items(), key=lambda item: item[1], reverse=True)

    response = []
    for disease_id, cf in sorted_results:
        disease = crud.get_disease(db, disease_id=disease_id)
        if disease:
            response.append(schemas.DiagnosisResult(
                disease=disease,
                certainty_factor=cf,
                percentage=round(cf * 100, 2)
            ))

    return response

@app.get("/api/diseases", response_model=List[schemas.Disease])
def read_diseases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_diseases(db, skip=skip, limit=limit)

@app.get("/api/diseases/{disease_id}", response_model=schemas.Disease)
def read_disease(disease_id: int, db: Session = Depends(get_db)):
    db_disease = crud.get_disease(db, disease_id=disease_id)
    if db_disease is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    return db_disease

# Mount static files at root
app.mount("/", StaticFiles(directory="static", html=True), name="static")
