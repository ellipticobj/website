import os
from flask import *
from flask_cors import *

app = Flask(__name__)
CORS(app)

projects = [
    {
        "name": "sigma",
        "description": "a simple programming language",
        "links": [
            {"label": "github", "url": "http://github.com/dimini171/sigma"}
        ]
    },
    {
        "name": "alpha",
        "description": "a stace oriented programming language",
        "links": [
            {"label": "github", "url": "https://github.com/ellipticobj/alpha"}
        ]
    },
    {
        "name": "cuter",
        "description": "a simple messenger app in the command line",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/cuter"}
        ]
    },
    {
        "name": "scrap",
        "description": "a small vim-like notetaking app in the terminal, made in python",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/scrap"}
        ]
    },
    {
        "name": "material you pomodoro timer",
        "description": "a pomodoro study timer app made using jetpack rompose in kotlin",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/studytimer"}
        ]
    },
    {
        "name": "random pip module",
        "description": "a small pip module that generates true random numbers using random.org's api",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/random-module"},
            {"label": "pypi", "url": "https://pypi.org/project/randomorg-api/"}
        ]
    },
    {
        "name": "password checker",
        "description": "small tool to check password strength or generate a new password",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/password-checker"}
        ]
    },
    {
        "name": "unit converter",
        "description": "a command line-based python program to convert different units or currencies",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/unit-converter"}
        ]
    },
    {
        "name": "this website",
        "description": "a small simple website that i made to learn static web development",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/ellipticobj.github.io"},
            {"label": "luna.hackclub.app", "url": "http://luna.hackclub.app"}
        ]
    },
    {
        "name": "my github readme",
        "description": "a readme for my github page that i used to learn more about gitHub actions",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/ellipticobj"},
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

if __name__ == '__main__':
    dev = True
    if dev:
        app.run(host='0.0.0.0', port=7272, debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
