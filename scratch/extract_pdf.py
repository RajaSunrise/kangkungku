from pypdf import PdfReader

def extract_text():
    reader = PdfReader("data-forward-chaining.pdf")
    text = ""
    for idx, page in enumerate(reader.pages):
        text += f"--- PAGE {idx+1} ---\n"
        text += page.extract_text() or ""
        text += "\n\n"
        
    with open("scratch/data-forward-chaining.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted {len(reader.pages)} pages to scratch/data-forward-chaining.txt")

if __name__ == "__main__":
    extract_text()
