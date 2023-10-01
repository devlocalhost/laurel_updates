import json

from flask import Flask, render_template

app = Flask(" -- laurel_updates -- ")

@app.route("/")
def main_route():
    return render_template("index.html")

@app.route("/roms")
def roms():
    with open('roms/a13/lineage.json', 'r') as json_file:
        data = json.load(json_file)

    return render_template("roms.html", data=data)

@app.route("/kernels")
def kernels():
    return render_template("kernels.html")
