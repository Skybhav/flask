from flask import Flask, render_template, redirect, flash, request
import sqlite3

app = Flask(__name__)
app.secret_key = 'TestSQLITE'


@app.route('/studentList')
@app.route('/')
def studentList():
    context = dict()

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall();

    context['students'] = rows

    return render_template('student_list.html', context=context)


@app.route('/addStudent', methods = ['GET', 'POST'])
def addStudent():
    context = dict()

    if request.method == 'POST':
        name = request.form.get('name', 'none')
        address = request.form.get('address', 'none')
        city = request.form.get('city', 'none')
        pin = request.form.get('pin', 'none')

        try:
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(name,address,city,pin) )
                con.commit()
                msg = "Record successfully added ..."
        except:
            msg = "Something went wrong ..."
        flash(msg)
    return render_template('student_add.html', context= context)



if __name__ == '__main__':
    app.debug = True
    app.run()
