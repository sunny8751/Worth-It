import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import database as db
import re


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
    oi_data = database_finder(oi)
    ci_data = database_finder(ci)
    print(oi_data)
    print(ci_data)
    # test: ci = coffee
    # implement a mongdb lookup to get the value of coffee
    
    if not ci_data or not oi_data:
        state = render_template('error')
    else:
        oi_price, oi_unit, oi_item = oi_data
        ci_price, ci_unit, ci_item = ci_data

        compared = oi_price / ci_price
        compared = str(round(compared, 2))
        state = render_template('state', oi_pass=oi_item, ci_pass=ci_item, ci_price=compared, ci_units=ci_unit)
    return statement(state)


@ask.intent("AddIntent", mapping={'name':'item_name', 'price':'item_price', 'unit': 'item_unit'})
def addToDB(name, price, unit):
    try:
        if not name:
            return statement(render_template('error'))
        if not unit:
            unit = "units"
        db.addMongoProduct(name, price, unit)
        resp = render_template('success', itemname=name)
    except:
        resp = render_template('error')
    return statement(resp)

@ask.intent("RemoveIntent", mapping={'name':'item_name'})
def removeDB(name):
    db.removeMongoProduct(name)
    remove = render_template('remove', itemname=name)
    return statement(remove)

# @ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
# def answer(first, second, third):
#     winning_numbers = session.attributes['numbers']
#     if [first, second, third] == winning_numbers:
#         msg = render_template('win')
#     else:
#         msg = render_template('lose')
#     return statement(msg)


def getShortenedName(itemName):
    CHARACTER_LIMIT = 40
    WORD_LIMIT = 6
    if len(itemName) > CHARACTER_LIMIT:
        tokens = [x for x in re.split(",| - |;|&|\||\)|\}| ", itemName) if len(x) > 0]
        # shorten item name using delimiters
        delimiterIndex = -1
        count = 0
        # find a suitable delimiter to cut off item's name at
        for i in range(len(tokens)):
            token = tokens[i]
            if (count + len(token) > CHARACTER_LIMIT):
                delimiterIndex = i
                break
            else:
                count += len(tokens)
        if delimiterIndex == -1 or delimiterIndex == 0:
            # reached end of string without finding a suitable delimiter
            # hard cutoff at word limit
            itemName = " ".join(tokens[:WORD_LIMIT])
        else:
            itemName = " ".join(tokens[:delimiterIndex])
    return itemName

def database_finder(inp):
    answer = mongodb_database_finder(inp)
    if answer:
        return answer
    # input didn't exist in mongodb database
    # so try to find in Amazon's database
    amazonAnswer = db.getAmazonProductInfo(inp)
    if not amazonAnswer:
        return None
    return (float(amazonAnswer[1])/100, "unit", getShortenedName(amazonAnswer[0]))

def mongodb_database_finder(inp):
    # get an array of words
    inp = inp.lower().split(" ")
    # generate all possible subsequences of words
    possible = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            possible.append(" ".join(inp[i:j]))
    print possible
    for item in possible:
        if (db.getMongoPrice(item) != "0"):
            value = db.getMongoPrice(item)
            unit = db.getMongoUnit(item)
            return (float(value), unit, item)
    return

if __name__ == '__main__':
    app.run(debug=True)