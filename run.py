from flask import Flask
import os
from website_package import website
import website_package
from alexa_package import alexa

app = Flask(__name__)

def run_app():
	app.register_blueprint(website)
	app.register_blueprint(alexa)
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, port=port)


if __name__ == "__main__":
	run_app()