from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
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
        name=request.form['name']
        email=request.form['email']
        age=request.form['age']
        phone=request.form['phone']
        course=request.form['course']
        print(name,email,age,phone,course)
        cur=mysql.connection.cursor()
        cur.execute(f'INSERT INTO student_data(name,email,age,phone_number,course) VALUES (%s, %s, %s, %s, %s)',(name,email,age,phone,course))
        mysql.connection.commit()
        cur.close()
    return redirect('/registered')

if __name__ == '__main__':
    app.run(debug=True)