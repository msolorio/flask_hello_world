from flask import Flask, url_for
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


with app.test_request_context():
    print('this will be printed automatically on save')
    print(url_for('hello_world'))
    print(url_for('fav_num', fav_num=12))


# Will run server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
