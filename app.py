''' This is the main file running the logic for the web app, using Flask to run routes '''

from flask import (
    Flask,
    render_template,
    #request,
)

# Configure application
app = Flask(__name__)

# global variables - dictionaries etc - reset at login &


@app.route("/", methods=["GET"])
def index():
    ''' Show's main page including upcoming race info '''

    return render_template(
        "index.html"
    )


@app.route("/cameras", methods=["GET"])
def cameras():
    ''' Show's main page including upcoming race info '''

    return render_template(
        "cameras.html",
    )

@app.route("/photographs", methods=["GET"])
def photographs():
    ''' Show's main page including upcoming race info '''

    return render_template(
        "photographs.html",
    )
