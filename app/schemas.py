from typing import List, Optional
from pydantic import BaseModel

class SymptomBase(BaseModel):
    code: str
    description: str
    image_url: Optional[str] = None

class Symptom(SymptomBase):
    id: int
    class Config:
        from_attributes = True

class DiseaseBase(BaseModel):
    name: str
    scientific_name: Optional[str] = None
    description: Optional[str] = None
    solution: Optional[str] = None
    image_url: Optional[str] = None

class Disease(DiseaseBase):
    id: int
    class Config:
        from_attributes = True

class UserSymptom(BaseModel):
    symptom_id: int
    confidence: float = 1.0  # User's confidence in observing this symptom (0.0 to 1.0)

class DiagnosisRequest(BaseModel):
    symptoms: List[UserSymptom]

class DiagnosisResult(BaseModel):
    disease: Disease
    certainty_factor: float
    percentage: float  # Display purpose
