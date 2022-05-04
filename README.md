# Cincinnatus Dev Portfolio made with Flask

This project is the result of a series of tutorials and courses I've taken on Cincinnatus.

**Live Preview:** [https://cincinnatus-portfolio.herokuapp.com/](https://cincinnatus-portfolio.herokuapp.com/)

## Screenshots

![Web Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Usage

### Clone the Repository

```bash
$ git clone https://github.com/adonyssantos/python-flask-website
$ cd python-flask-website
```

### Setup envoronment

```bash
$ pip install virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
```

#### To activate the virtual environment

```bash
$ source .venv/bin/activate
```

### Install Dependencies

```bash
$ pip install -r requirements.txt
```

### Run

#### Run in development mode

```bash
$ python run.py
```

#### Run in production mode

```bash
$ gunicorn app:app
```

## Authors

- [@adonyssantos](https://www.github.com/adonyssantos)

## License

[MIT](https://choosealicense.com/licenses/mit/)
