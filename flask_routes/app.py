from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() :
	return 'HOME'

@app.route('/hello')
def hello() :
	return "Hello World"

@app.route('/goodbye')
def goodbye() :
	return "Goodbye"

if __name__ == '__main__':
	app.run(debug=True)