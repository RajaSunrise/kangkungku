from typing import List, Optional
from pydantic import BaseModel, field_validator

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

# Aturan (Rules) Schemas
class AturanBase(BaseModel):
    penyakit_id: int
    gejala_id: int
    pakar_cf: float

    @field_validator('pakar_cf')
    @classmethod
    def validate_cf(cls, v):
        if not (0.0 <= v <= 1.0):
            raise ValueError('CF pakar harus antara 0.0 dan 1.0')
        return v

class AturanRead(AturanBase):
    id: int
    penyakit: Optional[Penyakit] = None
    gejala: Optional[Gejala] = None

    class Config:
        from_attributes = True

class DiagnosaHistoryRead(BaseModel):
    id: int
    user_id: Optional[int]
    penyakit: Penyakit
    faktor_kepastian: float
    persentase: float
    gejala_input: str
    created_at: str

    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_users: int
    total_diagnosa: int
    total_penyakit: int
    total_gejala: int
    total_aturan: int
    history_terbaru: List[DiagnosaHistoryRead]

class GejalaPengguna(BaseModel):
    gejala_id: int
    keyakinan: float = 1.0  # Keyakinan pengguna (0.0 to 1.0)

class PermintaanDiagnosa(BaseModel):
    gejala: List[GejalaPengguna]

class HasilDiagnosa(BaseModel):
    penyakit: Penyakit
    faktor_kepastian: float
    persentase: float

# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str
    alamat: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    alamat: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None

class UserRead(UserBase):
    id: int
    is_active: bool
    role: str

    class Config:
        from_attributes = True
