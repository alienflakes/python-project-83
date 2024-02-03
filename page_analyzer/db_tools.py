import psycopg2
from psycopg2.extras import NamedTupleCursor
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)


def db_execute(query, fetch=True, fetchall=False):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(query)
        if fetchall:
            return cursor.fetchall()
        elif fetch:
            return cursor.fetchone()
    return None


def get_url_by(param, value):
    query = f"SELECT * FROM urls WHERE {param} = '{value}' ;"
    return db_execute(query)


def get_all_urls():
    return db_execute("SELECT * FROM urls ;", fetchall=True)


def insert_url(name):
    date = datetime.date.today()
    query = f"""
            INSERT INTO urls (name, created_at)
            VALUES ('{name}', '{date}') ;
            """
    db_execute(query, fetch=False)
    return get_url_by('name', name)
