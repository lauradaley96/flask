from flask import Flask, render_template, request
import mysql.connector 
app=Flask(__name__)
db=mysql.connector.connect(host="localhost", user="root", password="root", database="project")

mycursor= db.cursor()

@app.route("/")
def homePage():
    mycursor.execute("Select * from personal")
    records=mycursor.fetchall();

    return render_template("HomePage.html", data=records)

@app.route("/departments/<dept>")
def departmentlist(dept):
    mycursor.execute("Select * from personal where departments='"+dept+"'") 
    records=mycursor.fetchall();

    return render_template("HomePage.html", data=records)
    
@app.route("/details/<EmployeeNo>")
def details(EmployeeNo):
    mycursor.execute("Select * from personal where EmployeeNo='"+EmployeeNo+"'")
    personalrecord=mycursor.fetchall();
    mycursor.execute("Select * from accounts where EmployeeNo='"+EmployeeNo+"'")
    salaryrecords=mycursor.fetchall()
    return render_template("details.html", personal=personalrecord,accounts=salaryrecords)

app.run(debug=True)