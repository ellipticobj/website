import subprocess
import threading
import os
from flask import *
from flask_socketio import *
from flask_cors import *

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

projects = [
    {
        "name": "cli messenger app",
        "description": "A simple messenger app in the command line made in Python.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/cli-messenger"}
        ]
    },
    {
        "name": "material you pomodoro timer",
        "description": "A pomodoro study timer app made using Jetpack Compose in Kotlin.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/studytimer"}
        ]
    },
    {
        "name": "random pip module",
        "description": "A small pip module that generates true random numbers using random.org's API.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/random-module"},
            {"label": "PyPI", "url": "https://pypi.org/project/randomorg-api/"}
        ]
    },
    {
        "name": "password checker",
        "description": "Small tool to check password strength or generate a new password.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/password-checker"}
        ]
    },
    {
        "name": "unit converter",
        "description": "A command line-based Python program to convert different units or currencies.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/unit-converter"}
        ]
    },
    {
        "name": "this website",
        "description": "A small simple website that I made to learn static web development.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/ellipticobj.github.io"},
            {"label": "ellipticobj.github.io", "url": "http://ellipticobj.github.io"},
            {"label": "luna.hackclub.app", "url": "http://luna.hackclub.app"}
        ]
    },
    {
        "name": "my github readme",
        "description": "A README for my GitHub page that I used to learn more about GitHub Actions.",
        "links": [
            {"label": "GitHub", "url": "http://github.com/ellipticobj/ellipticobj"},
            {"label": "ellipticobj.github.io/ellipticobj", "url": "http://ellipticobj.github.io/ellipticobj"}
        ]
    }
]

process = None

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projectspage():
    return render_template('projects.html', projects=projects)

@app.route('/getcode')
def getcode():
    file = request.args.get('file')
    project = "projects/example.py"
    filepath = os.path.join(project, file)
    if not filepath.startswith(os.path.abspath(project)):
        return "unauthorized", 403
    
    with open(filepath, 'r') as f:
        return f.read()

@app.route('/shells')
def shellpage():
    return render_template('shell.html')

@socketio.on('input', namespace='/shells') 
def handleshellinput(data):
    global process 
    if process is None:
        process = subprocess.Popen(
            ['/bin/bash'],
            cwd='projects/example',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        def readoutput():
            for line in iter(process.stdout.readline, ''):
                socketio.emit('output', {'data': line}, namespace='/shells')

        threading.Thread(target=readoutput(), daemon=True).start()

    if process.stdin:
        process.stdin.write(data + '\n')
        process.stdin.flush()

@socketio.on('disconnect', namespace='/shells')
def handledisconnect():
    global process
    if process:
        process.terminate()
        process = None

@socketio.on("runcmd")
def handlecommand(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        emit('output', result.decode())
        
    except Exception as e:
        emit('output', f'error: {e.output.decode()}')

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=7272, debug=True)
    