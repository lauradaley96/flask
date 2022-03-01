from flask import Flask, render_template, request, redirect
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

@app.route("/newrecord")
def newrecord():
    return render_template("inputform.html")

@app.route("/saverecord", methods=["post"])
def saverecord():
    name=request.form["na"]
    dept=request.form["dept"]
    sql1="insert into personal(name, department) values('{0}', '{1}')".format(name,dept)
    mycursor.execute(sql1)
    db.commit()
    return redirect("/")

@app.route("/showdepartment")
def showdepartment():
    return render_template("showdepartment.html")

@app.route("/showdepartmentEmployees", methods=["POST"])
def showdepartmentEmployees():
    dept=request.form["dept"]
    mycursor.execute("Select * from personal where department ='"+dept+"'")
    records=mycursor.fetchall();
    return render_template("HomePage.html", data=records)

    return dept

@app.route("/newpayslip")
def newpayslip():
    return render_template("newpayslip.html")

@app.route("/savepayslip", methods=["post"])
def savepayslip():
    Amount=request.form["Amount"]
    EmployeeNo=request.form["EmployeeNo"]
    sql1="insert into accounts(EmployeeNo, SalaryDate, Amount) values('{0}', now(), '{1}')".format(EmployeeNo, Amount)
    mycursor.execute(sql1)
    db.commit()
    return redirect("/")

app.run(debug=True)