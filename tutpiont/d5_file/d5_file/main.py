from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'ASFGH'
app.config['UPLOAD_FOLDER'] = './uploads'
# app.config['MAX_CONTENT_PATH'] = ''

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload_userfile', methods=['GET', 'POST'])
def upload_userfile():
    if request.method == 'POST':
        f = request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        flash('file uploaded successfully ... ')
    else:
        flash('Please select file and then upload ...')
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug = True
    app.run()