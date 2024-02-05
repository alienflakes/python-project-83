import psycopg2
from psycopg2.extras import NamedTupleCursor
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def db_connect():
    return psycopg2.connect(DATABASE_URL)


def db_execute(query, fetch=True, fetchall=False):
    with db_connect() as conn:
        cursor = conn.cursor(cursor_factory=NamedTupleCursor)
        cursor.execute(query)
        if fetchall:
            return cursor.fetchall()
        elif fetch:
            return cursor.fetchone()
    return None


def get_url_by(param, value, from_db='urls'):
    query = f"""SELECT * FROM {from_db} WHERE {param} = '{value}';
            """
    return db_execute(query)


def get_all_urls():
    query = """
            SELECT DISTINCT urls.id, urls.name,
            url_checks.created_at, url_checks.status_code
            FROM urls LEFT JOIN url_checks
            ON urls.id = url_checks.url_id
            ORDER BY urls.id DESC ;
            """
    return db_execute(query, fetchall=True)


def insert_url(name):
    date = datetime.date.today()
    query = f"""
            INSERT INTO urls (name, created_at)
            VALUES ('{name}', '{date}') ;
            """
    db_execute(query, fetch=False)
    return get_url_by('name', name)


def add_url_check(url_id, data):
    date = datetime.date.today()
    query = f"""
                INSERT INTO url_checks (url_id, status_code,
                h1, title, description, created_at)
                VALUES ({url_id}, {data['status_code']},
                '{data['h1']}', '{data['title']}',
                '{data['description']}', '{date}') ;
            """
    db_execute(query, fetch=False)
    return get_url_by('id', url_id, from_db='url_checks')


def get_url_checks(url_id):
    query = f"""SELECT * FROM url_checks WHERE url_id = '{url_id}'
            ORDER BY id DESC ;
            """
    return db_execute(query, fetchall=True)
