from flask import *
from flask_socketio import *
import subprocess

app = Flask(__name__)
app.config['SECRETKEY'] = "key"
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('run_command')
def run_command(data):
    command = data.get('command')
    try:
        result = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, text=True
        )
    except subprocess.CalledProcessError as e:
        result = e.output
    
    emit("command-result", {"result": result})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)