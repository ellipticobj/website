from flask import *
from flask_socketio import *
import subprocess
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

projects = [
    {"name": "CLI Messenger App", "description": "A simple messenger app in the command line made in Python.", "github": "http://github.com/ellipticobj/cli-messenger"},
    {"name": "Material You Pomodoro Timer", "description": "A pomodoro study timer app made using Jetpack Compose in Kotlin.", "github": "http://github.com/ellipticobj/studytimer"},
    {"name": "Random PIP Module", "description": "A small pip module that generates true random numbers using Random.org's API.", "github": "http://github.com/ellipticobj/random-module", "pypi": "https://pypi.org/project/randomorg-api/"},
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projectspage():
    return render_template('projects.html', projects=projects)
       
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=7272, debug=True)