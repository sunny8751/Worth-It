from flask import Flask
from website_package import website
import website_package
from alexa_package import alexa

app = Flask(__name__)

def run_app():
	app.register_blueprint(website)
	app.register_blueprint(alexa)
	app.run(debug=True)
	return url_for('website.index')


if __name__ == "__main__":
	run_app()