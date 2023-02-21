from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'd7_form'


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            flash('All data get successfully...')
            return render_template('success.html')
    return render_template('contact.html', form = form)



if __name__ == '__main__':
    app.debug = True
    app.run()

