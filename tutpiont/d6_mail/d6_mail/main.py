from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'EMAIL'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vaibhavtake905@gmail.com'
app.config['MAIL_PASSWORD'] = 'iyzqunabydvtyivb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/index')
def index():
    return render_template('mail_home.html')


@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        email = request.form.get('mail')
        recipients = [email]
        # recipients = ['vaibhavtake8@gmail.com']
        mail_msg = Message('Hello', sender='vaibhavtake905@gmail.com', recipients = recipients )
        mail_msg.body = 'Wellcome to test mail '
        # print('ffffffffffffff', mail_msg)

        mail.send(mail_msg)
        print('**************', mail)
        flash('Email send successfully ... ')
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()