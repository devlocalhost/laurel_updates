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

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import (
    Flask,
    request,
    render_template,
    make_response,
)

app = Flask(" -- laurel_updates -- ")

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

APP_SECRET_TOKEN = os.environ["APP_SECRET_TOKEN"]

if os.environ.get("LAUREL_MODE"):
    print("[DEBUG] Templates will auto reload")
    app.config["TEMPLATES_AUTO_RELOAD"] = True

commit_hash = os.environ.get('VERCEL_GIT_COMMIT_SHA')
commit_message = None

if commit_hash == None:
    commit_hash = subprocess.check_output(
        'git log -1 --pretty=format:"%h"', shell=True, text=True
    )

    commit_message = subprocess.check_output(
        f'git log -1 --pretty=format:%s {commit_hash}', shell=True, text=True
    )

utc_time = datetime.datetime.now(datetime.UTC).strftime("%A %B %-d, %I:%M:%S %p")
start_time = datetime.datetime.now()  # um... ^^^ ??
platform_details = f"{platform.uname()[1]} ({platform.uname()[2]})"
nl = "\n"
android_versions = ["roms/10", "roms/11", "roms/12", "roms/13", "roms/14", "roms/15"]


class CustomRenderer(mistune.HTMLRenderer):
    def heading(self, text, level):
        header_id = re.sub(r"\s+", "-", text.lower())
        return f'<h{level}>{text}</h{level}><div id="{header_id}"></div>'


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
        f"Hello world\nRunning on <code>{platform_details}</code>\nCommit: <code>{commit_hash}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit_hash}</code>)",
        -1002418052790,
        2
    )


def going_down():
    send_message(
        "[Going down]",
        f"GOODBYECRUELWORLD - <code>{platform_details}</code>\nCommit: <code>{commit_hash}</code> (<code>https://github.com/devlocalhost/laurel_updates/commit/{commit_hash}</code>)",
        -1002418052790,
        2
    )


def custom_header_plugin(md):
    md.renderer = CustomRenderer()


markdown_parser = mistune.create_markdown(plugins=[custom_header_plugin])


def list_json_files(directory):
    """get json files of dir"""

    json_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(filename)

    return json_files


def verify_signature(secret_token, signature_header, payload_body):
    if not signature_header:
        return False

    expected = (
        "sha256="
        + hmac.new(secret_token.encode(), payload_body, hashlib.sha256).hexdigest()
    )

    return hmac.compare_digest(expected, signature_header)


@app.route("/autod", methods=["POST"])
def autod():
    signature = request.headers.get("X-Hub-Signature-256")
    payload = request.get_data()

    if verify_signature(APP_SECRET_TOKEN, signature, payload):
        subprocess.Popen([os.path.abspath("auto-deploy.sh")])

        return "", 200

    else:
        return "", 403
    

@app.route("/")
def home():
    """home page"""

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

    countries_json = json.load(open("static/statistics/countries.json"))
    pages_json = json.load(open("static/statistics/pages.json"))

    return render_template("stats.html", data=[countries_json, pages_json, commit_hash, commit_message, platform_details, utc_time])


@app.route("/blog")
@app.route("/help")
def blogs():
    """blogs"""

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
def kernels_name(kernel_name):
    """kernels"""

    kernel_file = os.path.join("kernels", kernel_name + ".json")

    if not os.path.exists(kernel_file):
        return render_template("404.html")

    with open(kernel_file, encoding="utf-8") as file:
        data = json.load(file)

    return render_template("kernel_template.html", data=data)


@app.errorhandler(404)
def page_not_found(e):
    """404 page"""

    return render_template("404.html")


atexit.register(going_down)
starting()
