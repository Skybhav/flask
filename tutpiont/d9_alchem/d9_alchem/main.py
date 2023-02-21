from flask import Flask, flash, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'd9_alchem'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "dfdfdfd"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(1000))
    city = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    pin = db.Column(db.String(1000))

    def __init__(self, name, city, address, pin):
        self.name = name
        self.city = city
        self.address = address
        self.pin = pin

# db.create_all()

@app.route('/studentList')
@app.route('/')
def studentList():
    context = dict()

    context['students'] = Student.query.all()

    return render_template('student_list.html', context=context)


@app.route('/addStudent', methods = ['GET', 'POST'])
def addStudent():
    context = dict()

    if request.method == 'POST':
        name = request.form.get('name', 'none')
        address = request.form.get('address', 'none')
        city = request.form.get('city', 'none')
        pin = request.form.get('pin', 'none')

        # try:
        student = Student(name=name, city=city, address=address, pin=pin)
        db.session.add(student)
        db.session.commit()
        msg = "Student added successfully ."
        # except:
        #     msg = "Something went wrong ..."
        flash(msg)
    return render_template('student_add.html', context= context)



if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.debug = True
    app.run()
