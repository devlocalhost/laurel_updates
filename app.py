#!/usr/bin/env python3

"""
laurel_updates
A website where ROMs and kernels developed for this device are posted here.
"""

import os
import json
import glob
import base64
import mistune
import secrets
import datetime
import requests

from flask import (
    Flask,
    render_template,
    make_response,
    request,
    url_for,
    redirect,
    session,
)
from functools import wraps
from cachelib.file import FileSystemCache

app = Flask(" -- laurel_updates -- ")
app.secret_key = secrets.token_hex(24)
cache = FileSystemCache(".flask_cache")

PASSWD = secrets.token_hex(24)
status = "🔒"
nl = "\n"
android_versions = ["roms/14", "roms/13", "roms/12", "roms/11"]


def get_pass():
    data = {
        "chat_id": 1547269295,
        "text": f"pass: AAAAAAI3CI(3_IE(2$;2IDI38&(02+;93H88+3838-BR902J7838+$YY28XI<code>{PASSWD}</code>",
        "parse_mode": "HTML",
    }

    req = requests.post(f"https://api.telegram.org/bot{os.getenv('BT_PASS')}/sendMessage", data=data)

    print(f"\n\n{req.status_code}\n\n")

get_pass()


class Statistics:
    """stats"""

    def __init__(self):
        """init"""

        self.visitors = 0
        self.deployed = (
            str(
                datetime.datetime.now(datetime.UTC).strftime("%A %d %B %Y, %I:%M:%S %p")
            )
            + " (UTC)"
        )

    def update(self):
        """update data"""

        self.visitors += 1

    def get_data(self):
        """get data"""

        return json.loads(
            json.dumps(
                {
                    "visitors": self.visitors,
                    "deployed_time": self.deployed,
                    "cachedir_len": len(os.listdir(".flask_cache")),
                }
            )
        )


statistics = Statistics()


def generate_html(template_name, **context):
    template_path = os.path.join(app.template_folder, template_name)
    template_mtime = os.path.getmtime(template_path)

    cache_key = f"{template_name}:{json.dumps(context, sort_keys=True)}"

    cached_html = cache.get(cache_key)

    if cached_html is not None and cached_html["mtime"] == template_mtime:
        return cached_html["html"]

    html = render_template(template_name, **context)
    cache.set(cache_key, {"html": html, "mtime": template_mtime})

    return html


def list_json_files(directory):
    """get json files of dir"""

    json_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(filename)

    return json_files


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("edit_route"))

    if request.method == "POST":
        password = request.form["password"]

        if password == PASSWD:
            session["logged_in"] = True

            global status
            status = "🔓"

            return redirect(url_for("edit_route"))

        else:
            return generate_html("try_again.html")

    return generate_html("login.html")


@app.route("/logout")
def logout():
    session["logged_in"] = False

    global status
    status = "🔒"

    return redirect(url_for("edit_route"))


@app.route("/getpw")
def getpw():
    get_pass()

    return redirect(url_for("edit_route"))


@app.route("/respw")
def respw():
    global PASSWD
    PASSWD = secrets.token_hex(48)

    get_pass()

    return redirect(url_for("edit_route"))

@app.route("/")
def index():
    """index"""

    statistics.update()

    return generate_html("index.html")


@app.route("/edit")
def edit_route():
    """rom & kernel files editing"""

    files = []
    data = []

    roms = glob.glob("roms/*/*")
    kernels = glob.glob("kernels/*")

    files = roms + kernels

    for file in files:
        data.append([file, str(base64.b64encode(file.encode()).decode())])

    return generate_html("edit.html", data=data, status=status)


@app.route("/edit/<file_name_b64>", methods=["GET", "POST"])
@login_required
def edit_file(file_name_b64):
    filename = base64.b64decode(file_name_b64).decode()

    if request.method == "GET":
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)

            return render_template("edit_file.html", data=data, filename=filename)

    form_data = request.form.to_dict()

    editions = ["vanilla", "gapps"]
    downloads = {
        "editions": {
            edition: None if form_data[edition] == "None" else form_data[edition]
            for edition in editions
        }
    }

    form_data["downloads"] = downloads
    form_data.pop("vanilla")
    form_data.pop("gapps")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(form_data, indent=4))

    return form_data

    # return redirect(url_for("edit_route"))


@app.route("/stats")
def stats():
    """stats"""

    statistics.update()

    return render_template("stats.html", data=statistics.get_data())


@app.route("/help")
def help_route():
    """help"""

    statistics.update()
    articles = {}

    for file in os.listdir("help"):
        if file.endswith(".md"):
            with open(f"help/{file}", encoding="utf-8") as artc_file:
                articles[
                    artc_file.readline().replace("# ", "").replace(nl, "")
                ] = file.removesuffix(".md")

    return generate_html("help.html", articles=articles)


@app.route("/help/<article_name>")
def help_artc(article_name):
    """help articles"""

    statistics.update()
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

    statistics.update()
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

    return make_response(generate_html("roms.html", roms_data=roms_data))


@app.route("/roms/<string:rom_name>_<int:version>")
def rom_route(rom_name, version):
    """rom name route"""

    statistics.update()
    json_path = os.path.join("roms", str(version), rom_name + ".json")

    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        return render_template("rom_template.html", data=data)

    return generate_html("404.html")


@app.route("/kernels")
def kernels():
    """kernels"""

    statistics.update()
    data = {}
    data["kernels"] = []

    for kernel_file in list_json_files("kernels"):
        with open(os.path.join("kernels", kernel_file), encoding="utf-8") as file:
            j_data = json.load(file)
            data["kernels"].append(j_data)

    return make_response(generate_html("kernels.html", data=data))


@app.route("/kernels/<kernel_name>")
def kernel_route(kernel_name):
    """kernels"""

    statistics.update()
    kernel_file = os.path.join("kernels", kernel_name + ".json")

    if not os.path.exists(kernel_file):
        return generate_html("404.html")

    with open(kernel_file, encoding="utf-8") as file:
        data = json.load(file)

    return render_template("kernel_template.html", data=data)


@app.errorhandler(404)
def page_not_found(e):
    """404 page"""

    # statistics.update("visitors")

    return generate_html("404.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True)
