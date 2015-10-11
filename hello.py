from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')   

@app.route('/', methods=['POST'])
def file_upload():
    uploaded_files = request.files.getlist("all_images[]")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
        	filename = secure_filename(file.filename)
        	filenames.append(filename)
	        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html',filenames=filenames)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(debug=True)

