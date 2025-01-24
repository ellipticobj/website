from flask import *

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projectspage():
    return render_template('projects.html', projects=projects)
       
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=7272, debug=True)