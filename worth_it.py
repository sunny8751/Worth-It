import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import database as db


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return statement(welcome_msg)


@ask.intent("ConvertIntent" , mapping={'oi': 'original_item', 'ci': 'compared_item'})
def convert_intent(oi, ci):
    # test: oi = north face backpack
    # implement a search on amazon.com for the price of this item
    print(oi)
    print(ci)
    oi_data = db.getAmazonProductInfo(oi)
    ci_data = database_finder(ci.split(" "))
    print(oi_data)
    print(ci_data)
    # test: ci = coffee
    # implement a mongdb lookup to get the value of coffee
    
    if not ci_data or not oi_data:
        state = render_template('error')
    else:
        compared = ((int(oi_data[1]) / 100) / ci_data[0])
        compared = str(round(compared, 2))
        state = render_template('state', oi_pass=oi_data[0], ci_pass=ci_data[2], ci_price=compared, ci_units=ci_data[1])
    return statement(state)


@ask.intent("RemoveIntent", mapping={'name':'item_name'})
def addToDB(name):
    try:
        if not unit:
            unit = "units"
        db.addMongoProduct(name, price, unit)
        resp = render_template('success', itemname=name)
    except:
        resp = render_template('error')
    return statement(resp)

@ask.intent("AddIntent", mapping={'name':'item_name', 'price':'item_price', 'unit': 'item_unit'})

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
        if (db.getMongoPrice(item) != "0"):
            value = db.getMongoPrice(item)
            unit = db.getMongoUnit(item)
            return (float(value), unit, item)
    return

if __name__ == '__main__':
    app.run(debug=True)