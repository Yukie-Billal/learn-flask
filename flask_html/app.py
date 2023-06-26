from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() :
	return render_template('hello.html')

@app.route('/bye')
def bye() :
	return "<h1>BYE</h1>"

if __name__ == '__main__':
	app.run(debug=True)