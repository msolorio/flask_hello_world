from flask import Flask, url_for, request, render_template, redirect, abort
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


# Route parameters
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {escape(name)}'


# Type specific route parameters
# string, int, float, path, uuid
@app.route('/num/<int:fav_num>')
def fav_num(fav_num):
    return f'My favorite number is {fav_num}'


# Specifying the HTTP method
# By default, w/o specifying, route only handles GET
@app.route('/login')
def login_form():
    return { 'message': 'you requested the login form' }


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    
    return { 'message': 'you logged in' }

# Redirect
@app.route('/go-home')
def redirect_to_home():
    return redirect(url_for('hello_world'))

# Send error message
@app.route('/do-not-enter')
def do_not_enter():
    abort(403)


# Handle a page not found - 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# Can send response in a tuple form
# (response, status)
# (response, headers)
# (response, status, headers)


#############################################################
# Rendering templates
@app.route('/hello-template/')
@app.route('/hello-template/<name>')
def hello_template(name='Valued Customer'):
    return render_template('index.html', name=name)


# tells flask to behave as if it is handling a request
# will run on every file save
# with app.test_request_context():
#     print('this will be printed automatically on save')
#     print(url_for('hello_world'))
#     print(url_for('fav_num', fav_num=12))


# run server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
