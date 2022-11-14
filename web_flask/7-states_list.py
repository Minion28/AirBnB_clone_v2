#!/usr/bin/python3
'''
script that runs flask web app
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list():
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def exit(context):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
