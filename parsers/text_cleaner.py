import re

def clean_resume_text(text):

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Normalize bullet points
    text = text.replace("•", "-")

    # Normalize headings
    text = text.replace("EDUCATION", "Education")
    text = text.replace("EXPERIENCE", "Experience")
    text = text.replace("SKILLS", "Skills")

    # Remove unwanted symbols
    text = re.sub(r'[^\w\s\-\.,:/@]', '', text)

    return text.strip()