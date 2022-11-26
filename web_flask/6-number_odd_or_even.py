#!/usr/bin/python3
'''
do task 5
/number_odd_or_even/<n>: display a HTML page only if
n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
'''

from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', a=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oe(n):
    return render_template('6-number_odd_or_even.html', a=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
