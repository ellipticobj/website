from flask import *
from flask_socketio import *
import subprocess
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

'''
@app.route('/shells/example')
def projectshell(projname):
    projpath = os.path.join('projects', f"{projname}.py")

    if os.path.exists(projpath):
        return render_template('shell.html', projname=projname)
    else:
        return f"project {projname} not found", 404
'''

@socketio.on("execute")
def execute(data):
    projname = data.get('projname')
    command = data.get('command')
    
    projpath = os.path.join('projects', f"{projname}.py")
    
    if os.path.exists(projpath):
        process = subprocess.Popen(
            ['python3', projpath],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=command)
        emit('output', {'output': stdout or stderr})
    
    else:
        emit('output', {'output': f"error: project {projname} not found"})
        
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=7272)