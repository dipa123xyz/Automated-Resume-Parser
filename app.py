import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from db import get_db_connection, save_candidate
from parser import (
    extract_text_from_pdf,
    extract_name,
    extract_email,
    extract_phone,
    extract_education,
    extract_experience
)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():

    resume = request.files.get("resume")

    if resume is None:
        return "No file received"

    if resume.filename == "":
        return "No file selected"

    filename = secure_filename(resume.filename)

    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    resume.save(upload_path)

    text = extract_text_from_pdf(upload_path)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    education = ", ".join(extract_education(text))
    experience = ", ".join(extract_experience(text))

    skill_list = [
        "Python",
        "Machine Learning",
        "SQL",
        "Object-Oriented Programming",
        "Git",
        "GitHub",
        "NumPy",
        "Pandas",
        "Data Structures",
        "Artificial Intelligence",
        "Database"
    ]

    skills = [
        skill for skill in skill_list
        if skill.lower() in text.lower()
    ]

    skills = ", ".join(skills)

    save_candidate(
        name,
        email,
        phone,
        skills,
        education,
        experience,
        filename
    )

    return f"Resume parsed and saved successfully: {filename}"


@app.route("/candidates")
def candidates():

    search = request.args.get("search", "").strip()

    connection = get_db_connection()
    cursor = connection.cursor()

    if search:
        query = """
            SELECT * FROM candidates
            WHERE name ILIKE %s
               OR skills ILIKE %s
        """

        search_value = f"%{search}%"

        cursor.execute(
            query,
            (search_value, search_value)
        )

    else:
        cursor.execute(
            "SELECT * FROM candidates ORDER BY id DESC"
        )

    candidates_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "candidates.html",
        candidates=candidates_data
    )


if __name__ == "__main__":
    app.run(debug=True)