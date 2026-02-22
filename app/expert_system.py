from typing import List, Dict, Any
from .schemas import GejalaPengguna
from .models import Aturan

def hitung_diagnosa(gejala_pengguna: List[GejalaPengguna], semua_aturan: List[Aturan]) -> Dict[int, float]:
    """
    Menghitung Faktor Kepastian (Certainty Factor) untuk penyakit berdasarkan gejala pengguna dan aturan pakar.
    Mengembalikan dictionary {penyakit_id: faktor_kepastian}.
    """

    # Kelompokkan aturan berdasarkan penyakit
    aturan_per_penyakit: Dict[int, List[Aturan]] = {}
    for aturan in semua_aturan:
        if aturan.penyakit_id not in aturan_per_penyakit:
            aturan_per_penyakit[aturan.penyakit_id] = []
        aturan_per_penyakit[aturan.penyakit_id].append(aturan)

    # Map gejala pengguna untuk pencarian cepat: {gejala_id: keyakinan}
    map_gejala_pengguna = {g.gejala_id: g.keyakinan for g in gejala_pengguna}

    hasil = {}

    for penyakit_id, daftar_aturan in aturan_per_penyakit.items():
        cf_gabungan = 0.0

        for aturan in daftar_aturan:
            if aturan.gejala_id in map_gejala_pengguna:
                cf_pengguna = map_gejala_pengguna[aturan.gejala_id]
                cf_pakar = aturan.pakar_cf

                # CF untuk bukti spesifik ini
                cf_saat_ini = cf_pakar * cf_pengguna

                # Gabungkan menggunakan rumus CF: CF_baru = CF_lama + CF_saat_ini * (1 - CF_lama)

                if cf_saat_ini > 0:
                    cf_gabungan = cf_gabungan + cf_saat_ini * (1 - cf_gabungan)

        if cf_gabungan > 0:
            hasil[penyakit_id] = cf_gabungan

    return hasil
