# Ayo Ayco's personal site built with Flask

## Background
Yet another rewrite of my [personal site](https://ayo.ayco.io)

## Development -- needs Debian
1. Set up your machine. See [digitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04) (uses cookies)

    ```bash
    # update repositories
    $ sudo apt update

    # install python stuff
    $ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python-venv
    ```

2. Install dependencies

    ```bash
    # clone the project 
    $ git clone git@git.sr.ht:~ayoayco/ayco.io-flask

    # create python environment:
    $ python3 -m venv .venv

    # activate python env:
    $ . .venv/bin/activate

    # install wheel:
    $ pip install wheel

    # install gunicorn & flask:
    $ pip install gunicorn flask

    # rejoice!
    ```

3. To start development:
    1. allow port usage: `sudo ufw allow 5000`
    2. run the development server: `python api.py``
4. After development session, deactivate the python env with: `deactivate`
