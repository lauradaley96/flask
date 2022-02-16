from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
        return """
            <html>

            <center> <h1> welcome to my home page </h1> </center>
            We are the only building society in the United Kingdom
            <br>
            <br>
            <a> Who we are </a> <br>
            <a href ="http://localhost:5000/Services"> Our services </a> <br>
            </html>
            """

@app.route("/Team")
def message():
    return "<b> Hello </b> <u> everybody </u>"

@app.route("/Services")
def boom():
    return """
    <html>
    <h2> <center> We provide the following services </center> </h2>
    <br>
    <a href ="htt://localhost:5000"> Home </a>
    <br>
    <ul>
        <li> Open Account </li>
        <li> Deposit Money </li>
        <li> Withdraw Money </li>
    </ul>
    </html>
    """

app.run()