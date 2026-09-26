# Automated Resume Parser

An automated resume parsing web application built with Python, Flask, spaCy, PDFPlumber, and PostgreSQL.
## Features

- Upload PDF resumes
- Extract candidate name
- Extract email and phone number
- Extract skills
- Extract education
- Extract experience
- Store candidate information in PostgreSQL
- Search candidates by name or skill
## Technologies Used

- Python
- Flask
- spaCy
- PDFPlumber
- PostgreSQL
- psycopg2
- HTML
- CSS
## Project Structure

```text
Automated-Resume-Parser/
├── app.py
├── db.py
├── parser.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── templates/
├── static/
├── uploads/
└── venv/
## Database

Database name:

`resume_parser_db`

Table name:

`candidates`

The database stores candidate name, email, phone, skills, education, experience, and resume filename.
## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
Install the required packages:

```bash
pip install -r requirements.txt
Install the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
## Environment Variable

Create a `.env` file and add your PostgreSQL password:

```text
DB_PASSWORD=your_postgresql_password
## Run the Application

Start the Flask application:

```bash
python app.py
Then open the application in your browser:

http://127.0.0.1:5000