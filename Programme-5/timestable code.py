from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def homePage1():
    return render_template("homePage.html")

@app.route("/timestable/<num>")
def timesTable(num):
    return render_template("timestable.html", T=int(num))

app.run()