from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world() :
# 	return f"<h1>Hello, World!</h1>"


# @app.route("/<name>")
# def hello(name):
# 	return f"<h1>Hello, {escape(name)}</h1>"

# HTTP method
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# #  OR
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()


# Variable Rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# # Can use with resource management like create - edit
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'




@app.route('/')
def index():
    return '<h3>Index</h3>'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    url_for('static', filename='style.css')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


try:
    nama = 14
    print(f"nama saya {nama:%s}")
except Exception as e:
    Exception(e)