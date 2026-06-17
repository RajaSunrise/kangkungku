# Deploy ke Vercel

Panduan untuk mendeploy **KangkungKu** (FastAPI) ke Vercel.

## Prasyarat

- Akun [Vercel](https://vercel.com)
- Git repository (GitHub/GitLab/Bitbucket)

## Langkah Deployment

### 1. Konfigurasi Vercel

Buat file `vercel.json` di root proyek:

```json
{
  "buildCommand": "pip install -r requirements.txt",
  "outputDirectory": ".",
  "functions": {
    "api/index.py": {
      "runtime": "python3.12",
      "maxDuration": 30
    }
  },
  "routes": [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    { "src": "/(.*)", "dest": "/api/index.py" }
  ]
}
```

### 2. Entry Point untuk Serverless

Buat file `api/index.py`:

```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.main import app
```

### 3. Requirements.txt

Buat/update `requirements.txt` (Vercel membaca ini, bukan `pyproject.toml`):

```txt
fastapi>=0.131.0
uvicorn>=0.41.0
jinja2>=3.1.6
sqlalchemy>=2.0.46
python-dotenv>=1.2.2
python-multipart>=0.0.22
python-jose>=3.5.0
passlib[bcrypt]>=1.7.4
bcrypt==4.0.1
slowapi>=0.1.9
playwright>=1.58.0
```

> **Catatan**: Hapus `playwright` jika tidak digunakan di production untuk mempercepat build.

### 4. Database SQLite

Aplikasi sudah menggunakan SQLite secara default. Vercel memiliki **filesystem ephemeral** — data hanya bertahap selama fungsi berjalan, dan akan hilang saat fungsi cold start. Agar data seed tersedia, kita perlu memastikan SQLite file berada di jalur yang benar.

**Pastikan file `.env` tidak ada isinya atau tidak menyetel `DATABASE_URL`**, atau setel ke default SQLite:

```env
DATABASE_URL=sqlite:///./expert_system.db
```

> **PENTING**: Karena filesystem Vercel bersifat read-only (kecuali `/tmp`), untuk production sebaiknya gunakan database eksternal seperti PostgreSQL. SQLite hanya cocok untuk prototyping/demo.

### 5. Seed Database

Seed database **sebelum deploy** — file `expert_system.db` yang sudah di-seed harus ikut di-commit:

```bash
# Hapus DB lama (kalau ada)
rm -f expert_system.db

# Jalankan seed
uv run seed.py

# Commit database yang sudah di-seed
git add expert_system.db
git commit -m "Add seeded SQLite database"
```

### 6. Deploy ke Vercel

#### Via Vercel CLI:

```bash
npm install -g vercel
vercel login
vercel --prod
```

#### Via Vercel Dashboard:

1. Push kode ke GitHub/GitLab
2. Import repository di [vercel.com](https://vercel.com/new)
3. Framework pilih **Other**
4. Build Command: `pip install -r requirements.txt`
5. Deploy

### 7. Verify

Setelah deploy, buka URL yang diberikan Vercel. Aplikasi akan berjalan seperti biasa.

## Struktur File untuk Vercel

```
.
├── api/
│   └── index.py            # Entry point serverless
├── app/                    # Kode FastAPI
├── static/                 # File statis
├── templates/              # Jinja2 templates
├── expert_system.db        # Database SQLite (wajib di-commit)
├── vercel.json             # Konfigurasi Vercel
├── requirements.txt        # Dependensi Python
└── seed.py                 # Seeder database
```

## Troubleshooting

### Static files 404

Pastikan `vercel.json` memiliki route untuk `/static/(.*)` dan folder `static/` tidak di-ignore di `.vercelignore`.

### Database error: "no such table"

Pastikan `expert_system.db` sudah di-commit ke repository. Jika tidak, jalankan `uv run seed.py` dulu lalu commit.

### Module not found

Vercel membaca `requirements.txt`, bukan `pyproject.toml`. Pastikan semua dependensi tercantum di `requirements.txt`.

### Data hilang setelah beberapa saat

Ini behavior normal — SQLite di Vercel bersifat sementara karena filesystem ephemeral. Untuk data persisten, gunakan PostgreSQL (Neon/Supabase).
