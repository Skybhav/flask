from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/welcome/<name>')
def welcome(name):
    return f'welcome {name}'

@app.route('/add/<float:a>/<float:b>')
def add(a,b):
    sum = (a+b)
    return f'Sum of {a} and {b} = {sum}'


@app.route('/addint/<int:a>/<int:b>')
def addint(a,b):
    sum = (a+b)
    return f'Sum of {a} and {b} = {sum}'



@app.route('/test1')
def test1():
    return render_template('test1.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('************', request.form)
        return redirect(url_for('welcome', name=request.form.get('nm')))
    else:
        return redirect(url_for('test1'))


@app.route('/teststatic', methods=['GET'])
def teststatic():
     return render_template('static_test.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
