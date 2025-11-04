from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pages/quem_somos")
def sobre():
    return render_template("pages/quem_somos.html")

@app.route("/pages/contato")
def contato():
    return render_template("pages/contato.html")