from flask import Flask
from website_package import website
from alexa_package import alexa

app = Flask(__name__)
app.register_blueprint(website)
app.register_blueprint(alexa)
app.run(threaded=True)
# debug=True, 