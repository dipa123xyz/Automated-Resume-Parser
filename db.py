import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="resume_parser_db",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        port="5432"
    )

    return connection


def save_candidate(name, email, phone, skills, education, experience, resume_file):

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO candidates
        (name, email, phone, skills, education, experience, resume_file)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            name,
            email,
            phone,
            skills,
            education,
            experience,
            resume_file
        )
    )

    connection.commit()

    cursor.close()
    connection.close()