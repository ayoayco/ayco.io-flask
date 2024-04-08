# Ayo Ayco's personal site built with Flask

## Background
Yet another rewrite of my [personal site](https://ayo.ayco.io)

## Set up
1. Install Flask and dependencies. The following are the steps for MacOS/Linux:
    1. create python environment: `python3 -m venv .venv`
    2. activate python env: `. .venv/bin/activate`
    3. install wheel: `pip install wheel`
    4. install gunicorn & flask: `pip install gunicorn flask`
2. To start development:
    1. Set environment variable for the flask app entry point with `export FLASK_APP=api.py`
    2. run the development server: `flask run`; note that the default port (5000) needs to be open
3. After development session, deactivate the python env with: `deactivate`
