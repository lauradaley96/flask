from flask import Flask, render_template
app=Flask(__name__)

@app.route("/salaryslip")
def salaryslip():
    return render_template("salarySlip.html", name="Laura", salary=2000)


app.run()