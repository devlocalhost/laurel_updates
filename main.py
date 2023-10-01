import os
import json

from flask import Flask, render_template, jsonify

app = Flask(" -- laurel_updates -- ")

json_dir = 'roms/a13'

def list_json_files(directory):
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_files.append(filename)
    return json_files

for json_file in list_json_files(json_dir):
    rom_name = json_file.replace(".json", "")

    def json_route(filename):
        with open(os.path.join(json_dir, filename)) as file:
            data = json.load(file)

        return render_template(f"roms/{rom_name}.html", data=data)

    app.add_url_rule(f'/roms/{rom_name}', json_file, json_route, defaults={'filename': json_file})

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
