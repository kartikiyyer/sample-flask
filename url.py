from flask import Flask

app = Flask('__name__')

@app.route('/user/<uuid:user_uuid>')
def show_user_profile_by_uuid(user_uuid):
	# This method should preceed the below method as this url is more specific than the below one.
	return 'User by uuid %s' % user_uuid

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id
