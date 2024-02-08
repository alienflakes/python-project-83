## Page Analyzer 🔍👀
### A simple tool for SEO content analysis.
A website with fine SEO content makes its creator proud.
This little study project gets headers, titles and descriptions from a URL, as well as keeps track of your previous checks and informs you on possible errors.

### [✨ Check out SEO page analyzer! ✨](https://alienflakes-page-analyzer.onrender.com)

> [Third project](https://ru.hexlet.io/programs/python/projects/83) of [@Hexlet](https://ru.hexlet.io/) Python Course

Built on Python using Flask, Jinja2, Bootstrap and PostgreSQL with the help of various libs (such as validators, requests, dotenv, psycopg2 and beautifulsoup4)
>
### Getting started
#### Requirements: Python ^3.10, poetry, pip, PostgreSQL

1. **Download** or simply clone the rep

```shell
pip install --user git+https://github.com/alienflakes/python-project-83.git
```

2. **Create a .env file** in the root directory and add two variables:
```
DATABASE_URL=postgresql://{user}:{password}@{host}:{port}/{database}

SECRET_KEY={enter or generate a key for the Flask app}
```

3. **Build the project** (this installs dependencies and creates the database):
```shell
make build
```

4. **Run the server** with gunicorn:
```shell
make start
```
### And you're all set! Follow the link in the terminal to use the app ✨
>
#### Funky badges:
[![Actions Status](https://github.com/alienflakes/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alienflakes/python-project-83/actions)
[![flake8 linter](https://github.com/alienflakes/python-project-83/actions/workflows/flake8_linter.yml/badge.svg)](https://github.com/alienflakes/python-project-83/actions/workflows/flake8_linter.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/288c1444b0bd7e6feb5d/maintainability)](https://codeclimate.com/github/alienflakes/python-project-83/maintainability)