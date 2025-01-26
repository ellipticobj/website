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
@app.route('/projects/')
def projectspage():
    return render_template('projects.html', projects=projects)

@app.route('/projects/json')
@app.route('/projects/json/')
def projectsapi():
    projectdir = os.path.abspath('projects')
    return jsonify(projects)

@app.route('/shells')
@app.route('/shells/')
def shellpage():
    return render_template('shell.html')

@app.route('/dimini')
@app.route('/dimini/')
def dimini():
    return render_template('dimini.html')

@socketio.on('connect', namespace='/shells')
def onconnect():
    intro = '''welcome to the interactive shell!
'''

    socketio.emit('output', {'data': intro}, namespace='/shells')

@socketio.on('input', namespace='/shells') 
def handleinput(data):
    global process 
    projectdir = os.path.abspath('projects')
    
    if process is None:
        process = subprocess.Popen(
            ['/bin/bash'],
            cwd='projects/',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        def readoutput():
            global process

            try:
                for line in iter(process.stdout.readline, '\n'):
                    if line:
                        socketio.emit('output', {'data': line}, namespace='/shells')
                socketio.emit('output', {'data': '\n$ '}, namespace='/shells')
                
            except Exception as e:
                print(f"error at readoutput(): {e}")
                
            finally:
                if process:
                    process.stdout.close()
                    process.stdin.close()
                    process.terminate()
                    process = None
                socketio.emit('output', {'data': '\n$ '}, namespace='/shells')

        threading.Thread(target=readoutput(), daemon=True).start()
    
    if data.startswith("python "):
        script = data.split(" ")[1]
        scriptpath = os.path.abspath(os.path.join(projectdir, script))
        
        if scriptpath.startswith(projectdir) and os.path.exists(scriptpath):
            process.stdin.write(data + '\n')
            process.stdin.flush()
            
        else:
            socketio.emit('output', {'data': 'error: file not found or unauthorized\n'}, namespace='/shells')
    
    else:
        socketio.emit('output', {'data': 'error: only python scripts can be executed\n'}, namespace='/shells')
    
    if process.stdin:
        process.stdin.write(data + '\n')
        process.stdin.flush()
    else:
        socketio.emit('output', {'data': 'error: process not running\n'}, namespace='/shells')

@socketio.on('disconnect', namespace='/shells')
def handledisconnect():
    global process
    if process:
        try:
            process.terminate()
            process = None
        except Exception as e:
            print(f"error at handledisconnect(): {e}")

@app.route('/getcode')
def getcode():
    file = request.args.get('file', 'example.py')
    projectdir = os.path.abspath('projects')
    filepath = os.path.join(projectdir, file)

    if not filepath.startswith(projectdir):
        return "unauthorized", 403

    if not os.path.exists(filepath):
        return f"{file} not found", 404

    with open(filepath, 'r') as f:
        return f.read()

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=7272, debug=True)
    