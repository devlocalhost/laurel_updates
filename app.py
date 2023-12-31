#!/usr/bin/env python3

"""
laurel_updates
A website where ROMs and kernels developed for this device are posted here.
"""

import os
import json
import glob
import atexit
import base64
import mistune
import secrets
import platform
import datetime
import requests
import subprocess

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
cache = FileSystemCache(".flask_cache")

if os.getenv("LAUREL_MODE"):
    print("[DEBUG] Templates will (hopefully) auto reload")
    app.config["TEMPLATES_AUTO_RELOAD"] = True

commit = subprocess.check_output(
    'git log -1 --pretty=format:"%h"', shell=True, text=True
)
utc_time = datetime.datetime.now(datetime.UTC).strftime("%A %B %-d, %I:%M:%S %p")
start_time = datetime.datetime.now()  # um... ^^^ ??
platform_details = f"{platform.uname()[1]} ({platform.uname()[2]})"
nl = "\n"
android_versions = ["roms/14", "roms/13", "roms/12", "roms/11"]


def get_uptime():
    current_time = datetime.datetime.now()
    uptime_duration = current_time - start_time

    components = []
    days, seconds = uptime_duration.days, uptime_duration.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days > 0:
        components.append(f"{days} days")
    if hours > 0:
        components.append(f"{hours} hours")
    if minutes > 0:
        components.append(f"{minutes} minutes")
    if seconds > 0:
        components.append(f"{seconds} seconds")

    return str(", ".join(components)).strip()


def send_message(func, message):
    print(f"{func} - Sending message to dev...")

    data = {"chat_id": 1547269295, "text": message, "parse_mode": "HTML"}

    try:
        req = requests.post(
            f"https://api.telegram.org/bot{os.getenv('TKN')}/sendMessage", data=data
        )

        print(f"{func} - Status: {req.status_code}")

    except Exception as exc:
        print(f"{func} - ERR: {type(exc).__name__}")


def starting():
    send_message(
        "[Starting]",
        f"Hello world\nRunning on <code>{platform_details}</code>\nCommit: <code>{commit}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit}</code>)\n{utc_time} (UTC)",
    )


def going_down():
    send_message(
        "[Going down]",
        f"GOODBYECRUELWORLD - <code>{platform_details}</code>\nWas up for: <code>{get_uptime()}</code>\nCommit: <code>{commit}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit}</code>)\n{utc_time} (UTC)",
    )
    # send_message("[Going down]", f"GOODBYECRUELWORLD - <code>{platform_details}</code>\nWas up for: {get_uptime()}")


class Statistics:
    """stats"""

    def __init__(self):
        """init"""

        self.visitors = 0
        self.deployed = f"{utc_time} (UTC)"

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
                    "platform": platform_details,
                    "uptime": get_uptime(),
                    "commit": commit,
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


@app.route("/")
def home():
    """home page"""

    statistics.update()

    return generate_html("index.html")


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
def help_article(article_name):
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
def roms_name(rom_name, version):
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
def kernels_name(kernel_name):
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

    statistics.update()

    return generate_html("404.html")


atexit.register(going_down)
starting()
