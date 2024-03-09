from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
import os
app=Flask(__name__)
app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
app.config['MYSQL_USER']=os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB']='student_registration'
app.config['MYSQL_PORT']=3000

mysql=MySQL(app)

@app.route('/')
def registrationForm():
    return render_template('register.html')

@app.route('/registered')
def registered():
    return render_template('registered.html')

@app.route('/register',methods=['POST'])
def registration():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_no = request.form['phone_no']
        DOB = request.form['DOB']
        blood_group = request.form['blood_group']
        address = request.form['address']
        department = request.form['department']
        course = request.form['course']
        password=request.form['password']
        hashed_password = generate_password_hash(password)
        print(hashed_password)
        cur=mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students (name, email, age, father_name, mother_name, phone_no, DOB, blood_group, address, department, course,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
            (name, email, age, father_name, mother_name, phone_no, DOB, blood_group, address, department, course,hashed_password))
        mysql.connection.commit()
        cur.close()
    return redirect('/registered')

if __name__ == '__main__':
    app.run(debug=True)