#!/usr/bin/python3
'''
do task 2
/c/<text>: display “C ” followed by the value of the
 text variable (replace underscore _ symbols with a space )
 /python/(<text)
'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<Text>', strict_slashes=False)
def pyth(Text='is cool'):
    Text = Text.replace('_', ' ')
    return 'Python {}'.format(Text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
