from flask import Flask
import os
from website_package import website
import website_package
from alexa_package import alexa

app = Flask(__name__)
app.register_blueprint(website)
app.register_blueprint(alexa)
app.run(threaded=True)
# debug=True, 
