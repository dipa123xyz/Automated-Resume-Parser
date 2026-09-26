import pdfplumber
import spacy
import re


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities


def extract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    match = re.search(email_pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    phone_pattern = r'(?:\+91[\s-]?)?[6-9]\d{9}'

    match = re.search(phone_pattern, text)

    if match:
        return match.group()

    return None


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None
def extract_education(text):
    education_keywords = [
        "B.Tech",
        "B.E",
        "Bachelor",
        "B.Sc",
        "M.Tech",
        "M.E",
        "M.Sc",
        "MBA",
        "BCA",
        "MCA",
        "Computer Science",
        "Engineering"
    ]

    education = []

    for keyword in education_keywords:
        if keyword.lower() in text.lower():
            education.append(keyword)

    return list(dict.fromkeys(education))
def extract_experience(text):
    experience_keywords = [
        "Internship",
        "Intern",
        "Experience",
        "Work Experience",
        "Machine Learning Intern",
        "Software Intern",
        "Developer Intern"
    ]

    experience = []

    for keyword in experience_keywords:
        if keyword.lower() in text.lower():
            experience.append(keyword)

    return list(dict.fromkeys(experience))