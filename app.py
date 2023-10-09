"""
laurel_updates
A website where ROMs and kernels developed for this device are posted here.
"""

import os
import json
import time
import mistune
from flask import Flask, render_template, make_response

app = Flask(" -- laurel_updates -- ")
nl = "\n"
android_versions = ["roms/13", "roms/12", "roms/11"]


def list_json_files(directory):
    """get json files of dir"""

    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(filename)
    return json_files


@app.route("/")
def index():
    """index"""

    return render_template("index.html")


@app.route("/help")
def help_route():
    """help"""

    articles = {}

    for file in os.listdir("help"):
        if file.endswith(".md"):
            with open(f"help/{file}", encoding="utf-8") as artc_file:
                articles[artc_file.readline().replace("# ", "").replace(nl, "")] = file.removesuffix(".md")

    return render_template("help.html", articles=articles)

@app.route("/help/<article_name>")
def help_artc(article_name):
    """help articles"""

    article_file = os.path.join("help", article_name + ".md")

    if not os.path.exists(article_file):
        return render_template("404.html")

    with open(article_file, encoding="utf-8") as file:
        title = file.readline().removeprefix("# ").removesuffix(nl)
        data = mistune.html(file.read())

    return render_template("help_template.html", data=data, title=title)


@app.route("/roms")
def roms():
    """roms"""

    roms_data = {}

    for version in android_versions:
        version = version.split("/")[1]
        roms_directory = f"roms/{version}"
        roms_list = []

        for file in list_json_files(roms_directory):
            rom_name = file.removesuffix(".json")
            roms_list.append(rom_name)

            with open(
                os.path.join(roms_directory, file), encoding="utf-8"
            ) as json_file:
                data = json.load(json_file)
                data["route_name"] = (
                    rom_name.removesuffix(".json")
                    .removesuffix(" ")
                    .removesuffix("(")
                    .removesuffix(")")
                    + f"_{version}"
                )

            if version not in roms_data:
                roms_data[version] = []

            roms_data[version].append(data)

    return make_response(render_template("roms.html", roms_data=roms_data))


@app.route("/roms/<string:rom_name>_<int:version>")
def rom_route(rom_name, version):
    """rom name route"""

    json_path = os.path.join("roms", str(version), rom_name + ".json")

    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        return render_template("rom_template.html", data=data)

    return render_template("404.html")


@app.route("/kernels")
def kernels():
    """kernels"""

    data = {}
    data["kernels"] = []

    for kernel_file in list_json_files("kernels"):
        with open(os.path.join("kernels", kernel_file), encoding="utf-8") as file:
            j_data = json.load(file)
            data["kernels"].append(j_data)

    return make_response(render_template("kernels.html", data=data))


@app.route("/kernels/<kernel_name>")
def kernel_route(kernel_name):
    """kernels"""

    kernel_file = os.path.join("kernels", kernel_name + ".json")

    if not os.path.exists(kernel_file):
        return render_template("404.html")

    with open(kernel_file, encoding="utf-8") as file:
        data = json.load(file)

    return render_template("kernel_template.html", data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
