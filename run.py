from flask import Flask
from website import website
from alexa import alexa

app = Flask(__name__)
app.register_blueprint(website)
app.register_blueprint(alexa)
app.run(debug=True)