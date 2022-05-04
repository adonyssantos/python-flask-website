from app import app

PORT = 5000
DEBUG = True

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
