from app.database import SessionLocal
from app import models

db = SessionLocal()
d_count = db.query(models.Disease).count()
s_count = db.query(models.Symptom).count()
r_count = db.query(models.Rule).count()

print(f"Diseases: {d_count}")
print(f"Symptoms: {s_count}")
print(f"Rules: {r_count}")

db.close()
