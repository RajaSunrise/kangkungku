from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from .database import Base

class Disease(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    scientific_name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    solution = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)

    rules = relationship("Rule", back_populates="disease")


class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    image_url = Column(String, nullable=True)

    rules = relationship("Rule", back_populates="symptom")


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"))
    symptom_id = Column(Integer, ForeignKey("symptoms.id"))
    expert_cf = Column(Float)

    disease = relationship("Disease", back_populates="rules")
    symptom = relationship("Symptom", back_populates="rules")
