# Ayo Ayco's personal site built with Flask

## Background
Yet another rewrite of my [personal site](https://ayo.ayco.io)

## Set up -- needs Linux
1. Install dependencies
    1. create python environment: `python3 -m venv .venv`
    2. activate python env: `. .venv/bin/activate`
    3. install wheel: `pip install wheel`
    4. install gunicorn & flask: `pip install gunicorn flask`
2. To start development:
    1. allow port usage: `sudo ufw allow 5000`
    2. run the development server: `python api.py``
3. After development session, deactivate the python env with: `deactivate`
