# from flask import Flask

# app = Flask(__name__)
# from app import views


from flask import Blueprint

website = Blueprint('website', __name__)
import views