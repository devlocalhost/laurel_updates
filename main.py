from flask import Flask, render_template

app = Flask(" -- laurel_updates -- ")

@app.route("/")
def main_route():
    return render_template("index.html")
