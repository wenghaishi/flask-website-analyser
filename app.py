from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_index.html")


app.run(host="0.0.0.0", port=80)
