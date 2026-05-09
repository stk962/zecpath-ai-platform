import os

from parsers.pdf_extractor import extract_pdf_text
from parsers.docx_extractor import extract_docx_text
from parsers.text_cleaner import clean_resume_text


def parse_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    raw_text = ""

    if ext == ".pdf":
        raw_text = extract_pdf_text(file_path)

    elif ext == ".docx":
        raw_text = extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")

    cleaned_text = clean_resume_text(raw_text)

    return cleaned_text