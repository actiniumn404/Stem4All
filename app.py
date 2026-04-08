from flask import Flask, render_template, request, jsonify, make_response, redirect
from flask_frozen import Freezer

import sys

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

freezer = Freezer(app)


@app.route('/')
def page_home():
    return render_template("lander.html")


if __name__ == "__main__":
    if "DEBUG" in sys.argv:
        app.run(port=80, host="0.0.0.0")
    else:
        freezer.freeze()
