from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/student')
def student():
    context = dict()
    return render_template('student.html', context=context)


@app.route('/result', methods = ['POST', 'GET'])
def result():
    context = dict()
    result = list()
    if request.method == 'POST':
        result = request.form

    context['result'] = result
    return render_template('result.html', context=context)


if __name__ == '__main__':
    app.debug = True
    app.run()