from flask import Flask

__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def hey():
    return "let's get it"
