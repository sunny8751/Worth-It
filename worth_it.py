import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import database as db


connection = Connection()
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return statement(welcome_msg)


@ask.intent("ConvertIntent" , mapping={'oi': 'original_item', 'ci': 'compared_item'})
def next_round(oi, ci):
    # test: oi = north face backpack
    # implement a search on amazon.com for the price of this item
    print(oi)
    print(ci)
    test_oi_price = 50.00
    ci_price = database_finder(ci.split(" "))
    units = get_unit(ci.split(" "))

    # test: ci = coffee
    # implement a mongdb lookup to get the value of coffee
    

    compared = test_oi_price / ci_price
    state = render_template('state', oi_pass=oi, ci_pass=ci, ci_price=compared, ci_units=units)
    return statement(state)


# @ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
# def answer(first, second, third):
#     winning_numbers = session.attributes['numbers']
#     if [first, second, third] == winning_numbers:
#         msg = render_template('win')
#     else:
#         msg = render_template('lose')
#     return statement(msg)

def database_finder(inp):
    value = 0
    for item in inp:
        if (db.getMongoPrice(item) != 0):
            value = db.getMongoPrice(item)
    return value

def get_unit(inp):
    unit = ""
    for item in inp:
        if (db.getMongoUnit(item) != ""):
            unit = db.getMongoPrice(item)
    return unit

if __name__ == '__main__':
    app.run(debug=True)