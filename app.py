import os
from os.path import join, dirname, realpath
from flask import Flask, render_template, session, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import random, string

# Set upload storage path
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')

# Set allowed file extensions
ALLOWED_EXTENSIONS = set(['txt'])

# Configure application
app = Flask(__name__)

# Configure upload storage location
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure file size limit
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 # 100 KB Size Limit

# Set app secret key
app.secret_key = 'super secret key'

# Configure file extensions verification
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Generate random string with letters and numbers
def id_generator(size=16, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

"""Upload decorator"""
@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        file = request.files['file']

        # Check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        # Check if file does not exist
        if file.filename == '':
            flash('Please select a file')
            return redirect(request.url)

        # Check if extension is invalid
        if file and not allowed_file(file.filename):
            flash('This file type is not supported. Allowed file types: .txt')
            return redirect(request.url)

        # Check if file exists and extension is valid
        if file and allowed_file(file.filename):

            # Return a secure version of the file in an ASCII only string for maximum portability
            filename = secure_filename(file.filename)

            # Rename file
            newfilename = '%s_upload.%s'%(id_generator(), file.filename.split('.')[-1])

            # Save filename directly on the filesystem
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], newfilename))

            # Redirect user to uploads/filename
            return redirect(url_for('upload_success', filename=filename))

    return render_template('upload.html')

"""Success decorator"""
@app.route('/uploads')
def upload_success():
    return render_template('success.html')

"""RequestEntityTooLarge error handler decorator"""
@app.errorhandler(413)
def error413(e):
    return '''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title></title>
      </head>
      <body>
        <h1>Oops!</h1>
        <p>413 – Request Entity Too Large</p>
      </body>
    </html>
    '''
