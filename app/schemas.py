from typing import List, Optional
from pydantic import BaseModel

class GejalaBase(BaseModel):
    kode: str
    deskripsi: str
    url_gambar: Optional[str] = None

class Gejala(GejalaBase):
    id: int
    class Config:
        from_attributes = True

class PenyakitBase(BaseModel):
    nama: str
    nama_ilmiah: Optional[str] = None
    deskripsi: Optional[str] = None
    solusi: Optional[str] = None
    url_gambar: Optional[str] = None

class Penyakit(PenyakitBase):
    id: int
    class Config:
        from_attributes = True

class GejalaPengguna(BaseModel):
    gejala_id: int
    keyakinan: float = 1.0  # Keyakinan pengguna (0.0 to 1.0)

class PermintaanDiagnosa(BaseModel):
    gejala: List[GejalaPengguna]

class HasilDiagnosa(BaseModel):
    penyakit: Penyakit
    faktor_kepastian: float
    persentase: float
