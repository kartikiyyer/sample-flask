from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask('__name__')

@app.route('/avatar', methods=['POST'])
def upload_avatar():
	f = request.files['file']
	f.save('/Users/kiyyer/Documents/%s' % f.filename)
	return f.filename

@app.route('/file', methods=['POST'])
def upload_file():
	f=request.files['file']
	f.save('/Users/kiyyer/Documents/%s' % secure_filename(f.filename))
	return f.filename