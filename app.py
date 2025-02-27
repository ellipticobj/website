from flask import Flask, render_template, jsonify
from flask_cors import CORS

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
        "name": "cuter",
        "description": "a simple messenger app in the command line",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/cuter"}
        ]
    },
    {
        "name": "meow",
        "description": "a 'replacement' for git's push, pull and commit commands i made for myself",
        "links": [
            {"label": "github", "url": "http://github.com/ellipticobj/meower"}
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
        "name": "alpha",
        "description": "a stack oriented programming language",
        "links": [
            {"label": "github", "url": "https://github.com/ellipticobj/alpha"}
        ]
    },
    {
        "name": "AI documentation generator",
        "description": "a program that analyzes code and uses ai to generate documentation for it",
        "links": [
            {"label": "github", "url": "http://github.com/nns-development/documentation-generator"}
        ]
    },
    {
        "name": "rng pip module",
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
    dev = False
    if dev:
        app.run(host='0.0.0.0', port=7272, debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=7272)
