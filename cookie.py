from flask import Flask, request

app = Flask('__name__')

@app.route('/')
def index():
	# Create and store a cookie in Postman. The try to retrieve it.
	print request.cookies.get('Cookie_1')
	return ''