from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from .database import Base

class Penyakit(Base):
    __tablename__ = "penyakit"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    nama_ilmiah = Column(String, nullable=True)
    deskripsi = Column(Text, nullable=True)
    solusi = Column(Text, nullable=True)
    url_gambar = Column(String, nullable=True)

    aturan = relationship("Aturan", back_populates="penyakit")


class Gejala(Base):
    __tablename__ = "gejala"

    id = Column(Integer, primary_key=True, index=True)
    kode = Column(String, unique=True, index=True)
    deskripsi = Column(String, index=True)
    url_gambar = Column(String, nullable=True)

    aturan = relationship("Aturan", back_populates="gejala")


class Aturan(Base):
    __tablename__ = "aturan"

    id = Column(Integer, primary_key=True, index=True)
    penyakit_id = Column(Integer, ForeignKey("penyakit.id"))
    gejala_id = Column(Integer, ForeignKey("gejala.id"))
    pakar_cf = Column(Float)

    penyakit = relationship("Penyakit", back_populates="aturan")
    gejala = relationship("Gejala", back_populates="aturan")
