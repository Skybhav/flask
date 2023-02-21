from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student_form():
    context = dict()
    return render_template('student_form.html', context=context)


@app.route('/student_result', methods = ['GET', 'POST'])
def student_result():
    print('*****', request.form, request.method )
    context = dict()
    fdata = None
    if request.method == 'POST':
        fdata = request.form
        print('***************', request.form)
    context['formdata'] = fdata
    return render_template('student_result.html', context=context)



if __name__ == '__main__':
    app.debug = True
    app.run()