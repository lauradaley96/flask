from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/Team")
def message():
    return render_template("message.html")
    
@app.route("/Services")
def boom():
    return render_template("services.html")

app.run()