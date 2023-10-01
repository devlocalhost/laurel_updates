from flask import Flask, render_template

app = Flask(" -- laurel_updates -- ")

@app.route("/")
def main_route():
    return render_template("index.html")

@app.route("/roms")
def roms():
    return render_template("roms.html")

@app.route("/kernels")
def kernels():
    return render_template("kernels.html")
