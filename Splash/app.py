from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'

@app.route('/hello', methods=['GET'])
def say_hello():
	return 'Hello World!'

if __name__ == '__main__':
	app.run(debug=True)