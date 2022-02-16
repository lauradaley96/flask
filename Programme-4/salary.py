from flask import Flask, render_template
app=Flask(__name__)

@app.route("/info1/<name1>/<salary1>")
def homePage1(name1, salary1):

    return render_template("salarySlip.html", name=name1, salary=int(salary1))


app.run()