# Ayo Ayco's personal site built with Flask

## Background
Yet another rewrite of my [personal site](https://ayo.ayco.io)

## Development -- needs Debian
1. Set up your machine. See [digitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04) (uses cookies)

    ```bash
    $ sudo apt update
    $ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
    ```

2. Install dependencies
    1. create python environment: `python3 -m venv .venv`
    2. activate python env: `. .venv/bin/activate`
    3. install wheel: `pip install wheel`
    4. install gunicorn & flask: `pip install gunicorn flask`
3. To start development:
    1. allow port usage: `sudo ufw allow 5000`
    2. run the development server: `python api.py``
4. After development session, deactivate the python env with: `deactivate`
