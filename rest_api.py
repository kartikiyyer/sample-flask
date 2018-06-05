from flask import Flask, request

app = Flask('__name__')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'This is a post of login.'
	else:
		return 'This is a get of login.'

@app.route('/register', methods=['POST'])
def register():
	if request.method == 'POST':
		return '%s:%s' % (request.form['username'], request.form['password'])

@app.route('/echo')
def echo():
	return '%s %s' % (request.args['firstname'], request.args['lastname'])
