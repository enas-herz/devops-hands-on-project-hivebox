from flask import Flask
from project import VERSION

app = Flask(__name__)

@app.route("/version")
def print_version():
    return {"version":VERSION}