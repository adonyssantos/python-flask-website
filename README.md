# Cincinnatus Dev Portfolio made with Flask

This project is the result of a series of tutorials and courses I've taken on Cincinnatus.

**Live Preview:** [https://cincinnatus-portfolio.herokuapp.com/](https://cincinnatus-portfolio.herokuapp.com/)

## Screenshots

![image](https://user-images.githubusercontent.com/58638286/170557223-07a6123b-88be-4f4c-920d-6b670aa9e1f1.png)

![image](https://user-images.githubusercontent.com/58638286/170557288-3921a308-b7b3-4c2d-b99f-1af495e8c459.png)


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

#### To deactivate the virtual environment

```bash
$ deactivate
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
