from unicodedata import name
from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def open():
    return render_template("index.html")

@app.route("/home")
def hom():
    return render_template("home.html")
@app.route("/firstPerson")   
def fp():
    return render_template("FP.html")
@app.route("/action")
def action():
    return render_template("action.html")
app.run(debug=True)