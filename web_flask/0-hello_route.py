#!/usr/bin/python3
""" Starts Flask application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
