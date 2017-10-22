from flask import Flask
from website_package import website
from alexa_package import alexa

app = Flask(__name__)

def run_app():
	app.register_blueprint(website)
	app.register_blueprint(alexa)
	app.run(debug=True)

if __name__ == "__main__":
	run_app()