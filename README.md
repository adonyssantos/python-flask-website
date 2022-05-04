# Python App Portfolio

This project is the result of a series of tutorials and courses I've taken on Cincinnatus.

## Clone the Repository

```bash
$ git clone https://github.com/adonyssantos/python-flask-website
$ cd python-flask-website
```

## Setup envoronment

```bash
$ pip install virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
```

### To activate the virtual environment

```bash
$ source .venv/bin/activate
```

## Install Dependencies

```bash
$ pip install -r requirements.txt
```

## Run

### Run in development mode

```bash
$ python run.py
```

### Run in production mode

```bash
$ gunicorn app:app -b
```
