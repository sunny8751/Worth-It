from flask import Flask
from website_package import website
import website_package
from alexa_package import alexa

app = Flask(__name__)

def run_app():
	app.register_blueprint(website)
	app.register_blueprint(alexa)
	app.run(debug=True)
	return rederict("https://secure-sands-99264.herokuapp.com/website")

if __name__ == "__main__":
	run_app()