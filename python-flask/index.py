from flask import Flask, __version__
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Python with Flask version " + __version__ + " on Now 2.0"
