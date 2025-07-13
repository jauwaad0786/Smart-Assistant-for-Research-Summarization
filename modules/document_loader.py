# modules/document_loader.py

import fitz  # PyMuPDF
import os

def load_document(file):
    ext = os.path.splitext(file.name)[-1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file)
    elif ext == ".txt":
        return extract_text_from_txt(file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_txt(file):
    return file.read().decode("utf-8")
