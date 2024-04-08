# Flask server for my personal site

## Background

This is the default server running at [https://ayo.ayco.io](https://ayco.io). Currently its main responsibility is serving static files generated with Astro SSG which I maintain in a [separate project](https://ayco.io/sh/ayco.io-astro). The generated files from that project will populate a `dist` directory in here, which will then be served as-is.

My main motivation for running my personal site behind this Flask server is to easily develop REST APIs later in the `/api` route using Python. I didn't want to use the default Astro production server for this as I am looking to work with Python more.

## Development

1. Set up your **Debian** (for MacOS, search for counterpart instructions)

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
    (.venv)$ flask --app web.py --debug run
    ```

    > Note: On a Mac, the default port 5000 is used by AirDrop & Handoff; you may have to turn those off

4. Populate a `dist` directory with static files (e.g., `*.html` for pages). Currently I generate static files in a separate [Astro site project](https://ayco.io/sh/ayco.io-astro) -- see instructions on how to set it up separately, run the build script and copy the `dist` here.

4. After development session, deactivate the python env
    ```bash
    (.venv)$ deactivate
    ```

## Deployment

For deployment, the recommended setup is with production server `gunicorn` and reverse proxy `nginx`. See the [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04) (their website uses cookies).
