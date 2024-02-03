from flask import (Flask, render_template, request, redirect,
                   url_for, flash, get_flashed_messages)
import os
from urllib.parse import urlparse
from validators.url import url as validate_url
from dotenv import load_dotenv
from page_analyzer import db_tools


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'index.html',
        messages=messages
    )


@app.post('/urls')
def add_url():

    url_to_check = request.form.get('url')
    parsed_url = urlparse(url_to_check)
    normalized_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    if not validate_url(normalized_url):
        flash('Некорректный URL', 'danger')
        messages = get_flashed_messages(with_categories=True)
        return render_template('index.html', messages=messages), 422

    url = db_tools.get_url_by('name', normalized_url)
    if url:
        flash('Страница уже существует', 'warning')
        return redirect(url_for('url_page', id=url.id))
    url = db_tools.insert_url(normalized_url)
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('url_page', id=url.id))


@app.get('/urls')
def urls():
    messages = get_flashed_messages(with_categories=True)
    all_urls = db_tools.get_all_urls()
    return render_template('urls.html',
                           messages=messages, urls=all_urls[::-1])


@app.get('/urls/<int:id>')
def url_page(id):
    messages = get_flashed_messages(with_categories=True)
    url = db_tools.get_url_by('id', id)
    if not url:
        flash('Запрашиваемая страница не найдена', 'warning')
        return redirect(url_for('index'), 404)
    return render_template('url_page.html',
                           messages=messages, url=url)
