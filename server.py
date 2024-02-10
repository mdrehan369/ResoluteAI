from flask import Flask, render_template, request
from user import getDataFromModel

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/task1")
def task1():
    return render_template("task1.html", data="")


@app.route("/task2")
def task2():
    return render_template("task2.html")



@app.route("/getData", methods= ['POST'])
def getData():
    row = request.form['row']
    data = getDataFromModel(row)
    return render_template("task1.html", data=data)

if(__name__ == "__main__"):
    app.run(debug=True)


