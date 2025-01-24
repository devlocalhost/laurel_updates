#!/usr/bin/env python3

"""
laurel_updates
A website where ROMs and kernels developed for this device are posted here.
"""

import re
import os
import json
import atexit
import datetime
import subprocess

import mistune
import platform
import requests
import subprocess

from flask import (
    Flask,
    render_template,
    make_response,
)

app = Flask(" -- laurel_updates -- ")

if os.getenv("LAUREL_MODE"):
    print("[DEBUG] Templates will auto reload")
    app.config["TEMPLATES_AUTO_RELOAD"] = True

try:
    commit = subprocess.check_output(
        'git log -1 --pretty=format:"%h"', shell=True, text=True
    )

except:
    try:
        commit = os.environ["VERCEL_GIT_COMMIT_SHA"]

    except:
        commit = "Unknown"

utc_time = datetime.datetime.now(datetime.UTC).strftime("%A %B %-d, %I:%M:%S %p")
start_time = datetime.datetime.now()  # um... ^^^ ??
platform_details = f"{platform.uname()[1]} ({platform.uname()[2]})"
nl = "\n"
android_versions = ["roms/10", "roms/11", "roms/12", "roms/13", "roms/14", "roms/15"]


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


def send_message(func, message, chat_id=1547269295, message_thread_id=None):
    print(f"{func} - Sending message to dev...")

    data = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}

    if message_thread_id:
        data["message_thread_id"] = message_thread_id

    try:
        req = requests.post(
            f"https://api.telegram.org/bot{os.getenv('TKN')}/sendMessage",
            data=data,
            timeout=10,
        )

        print(f"{func} - Status: {req.status_code}\n{req.text}")

    except Exception as exc:
        print(f"{func} - ERR: {type(exc).__name__}")


def starting():
    send_message(
        "[Starting]",
        f"Hello world\nRunning on <code>{platform_details}</code>\nCommit: <code>{commit}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit}</code>)\n{utc_time} (UTC)",
        -1002418052790,
        2
    )


def going_down():
    send_message(
        "[Going down]",
        f"GOODBYECRUELWORLD - <code>{platform_details}</code>\nWas up for: <code>{get_uptime()}</code>\nCommit: <code>{commit}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit}</code>)\n{utc_time} (UTC)",
        -1002418052790,
        2
    )


class Statistics:
    """stats"""

    def __init__(self):
        """init"""

        self.visitors = 0
        self.deployed = f"{utc_time} (UTC)"
        self.rom_statistics = {
            "crDroid_10": {"views": 0},
            "LineageOS_11": {"views": 0},
            "PixelExperience_11": {"views": 0},
            "AospExtended_12": {"views": 0},
            "PixelOS_12": {"views": 0},
            "LineageOS_13": {"views": 0},
            "PixelExperience_13": {"views": 0},
            "PixelExperiencePlus_13": {"views": 0},
            "PixelOS_13": {"views": 0},
            "SparkOS_13": {"views": 0},
            "EvolutionX_14": {"views": 0},
            "LineageOS_14": {"views": 0},
            "PixelMagic_14": {"views": 0},
            "TequilaOS_14": {"views": 0},
            "ProjectBlaze_14": {"views": 0},
            "ProjectMatrixx_14": {"views": 0},
            "RisingOS_14": {"views": 0},
            "DerpFest_14": {"views": 0},
            "crDroid_14": {"views": 0},
            "crDroid_U_14": {"views": 0},
            "TheParasiteProject_14": {"views": 0},
            "AOSP_15": {"views": 0},
            "crDroid_15": {"views": 0},
            "DerpFest_15": {"views": 0},
            "LineageOS_15": {"views": 0},
            "ParanoidAndroid_15": {"views": 0},
            "PixelMagic_15": {"views": 0},
            "PixelOS_15": {"views": 0},
            "ProjectPixelage_15": {"views": 0},
            "YAAP_15": {"views": 0},
            # "": {"views": 0},
        }

    def update(self):
        """update data"""

        self.visitors += 1

    def rom_update(self, name):
        self.rom_statistics[name]["views"] += 1

    def get_data(self):
        """get data"""

        return json.loads(
            json.dumps(
                {
                    "visitors": self.visitors,
                    "deployed_time": self.deployed,
                    "platform": platform_details,
                    "uptime": get_uptime(),
                    "commit": commit,
                    "rom_hits": self.rom_statistics,
                }
            )
        )


class CustomRenderer(mistune.HTMLRenderer):
    def heading(self, text, level):
        header_id = re.sub(r"\s+", "-", text.lower())
        return f'<h{level}>{text}</h{level}><div id="{header_id}"></div>'


def custom_header_plugin(md):
    md.renderer = CustomRenderer()


markdown_parser = mistune.create_markdown(plugins=[custom_header_plugin])
statistics = Statistics()


def list_json_files(directory):
    """get json files of dir"""

    json_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(filename)

    return json_files


@app.route("/.well-known/discord")
def verify():
    """used to verify the domain for discord"""

    return "dh=8f0a33d72181fd1eb73a66321a42e5855556c7a1"


@app.route("/")
def home():
    """home page"""

    statistics.update()
    pattern = r'\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b'
    headline = "News."

    with open("blogs/news.md") as lines:
        lines = lines.readlines()
        headline_num = 1
        headline_link = lines[3].split("](")[1].strip().strip(")")

        for line_number, line in enumerate(lines):
            if not line.lstrip().startswith('-') and re.search(pattern, line):
                headline_num = line_number
                break

        headline = lines[headline_num].replace("## ", "")

    return render_template("index.html", headline=headline, headline_link=headline_link)


@app.route("/stats")
def stats():
    """stats"""

    statistics.update()

    return render_template("stats.html", data=statistics.get_data())


@app.route("/blog")
@app.route("/help")
def blogs():
    """blogs"""

    statistics.update()
    articles = {}

    for file in os.listdir("blogs"):
        if file.endswith(".md"):
            with open(f"blogs/{file}", encoding="utf-8") as artc_file:
                articles[artc_file.readline().replace("# ", "").replace(nl, "")] = (
                    file.removesuffix(".md")
                )

    return render_template("blog.html", articles=articles)


@app.route("/help/<article_name>")
@app.route("/blog/<article_name>")
def get_blog(article_name):
    """help articles"""

    statistics.update()
    article_file = os.path.join("blogs", article_name + ".md")

    if not os.path.exists(article_file):
        return render_template("404.html")

    with open(article_file, encoding="utf-8") as file:
        title = file.readline().removeprefix("# ").removesuffix(nl)
        data = markdown_parser(file.read())

    return render_template("blog_template.html", data=data, title=title)


@app.route("/roms")
def roms():
    """roms"""

    statistics.update()
    roms_data = {}

    for version in android_versions:
        version = version.split("/")[1]
        roms_directory = f"roms/{version}"

        for file in list_json_files(roms_directory):
            rom_name = file.removesuffix(".json")

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

            # if not data["archived"]:
            roms_data[version].append(data)

    return make_response(render_template("roms.html", roms_data=roms_data))


@app.route("/roms/<string:rom_name>_<int:version>")
def roms_name(rom_name, version):
    """rom name route"""

    statistics.update()
    json_path = os.path.join("roms", str(version), rom_name + ".json")

    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        statistics.rom_update(f"{rom_name}_{version}")

        return render_template("rom_template.html", data=data)

    return render_template("404.html")


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

    return make_response(render_template("kernels.html", data=data))


@app.route("/kernels/<kernel_name>")
def kernels_name(kernel_name):
    """kernels"""

    statistics.update()
    kernel_file = os.path.join("kernels", kernel_name + ".json")

    if not os.path.exists(kernel_file):
        return render_template("404.html")

    with open(kernel_file, encoding="utf-8") as file:
        data = json.load(file)

    return render_template("kernel_template.html", data=data)


@app.errorhandler(404)
def page_not_found(e):
    """404 page"""

    statistics.update()

    return render_template("404.html")


atexit.register(going_down)
starting()
