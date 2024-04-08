# Ayo Ayco's personal site built with Flask

## Background
Yet another rewrite of my [personal site](https://ayo.ayco.io)

## Development -- needs Linux / MacOS
1. Set up your machine

    ```bash
    # update repositories
    $ sudo apt update

    # install python stuff
    $ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv
    ```

2. Install dependencies

    ```bash
    # clone the project 
    $ git clone git@git.sr.ht:~ayoayco/ayco.io-flask

    # go into the project directory
    $ cd ayco.io-flask

    # create python environment:
    $ python3 -m venv .venv

    # activate python env:
    $ . .venv/bin/activate

    # install wheel:
    (.venv)$ pip install wheel

    # install gunicorn & flask:
    (.venv)$ pip install flask

    # rejoice!
    ```

3. To start development, run the following:
    ```bash
    (.venv)$ python api.py
    ```

    > Note: On a Mac, the default port 5000 is used by AirDrop & Handoff; you may have to turn those off

4. After development session, deactivate the python env with: `deactivate`

## Deployment

For deployment, the recommended setup is with production server `gunicorn` and reverse proxy `nginx`. See the [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04) (their website uses cookies).
