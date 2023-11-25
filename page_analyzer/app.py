from flask import Flask, render_template

__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template(
        'index.html'
    )
