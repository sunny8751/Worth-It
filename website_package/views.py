from flask import render_template
# import HTMLParser
import json
import time
# from app import app

from website_package import website

question = None
answer = None

@website.route('/website')
@website.route('/index')
def index():
   	return render_template('website/index.html',title='Worth It?')

@website.route('/question_poll')
def questionPoll():
	global question
	#remove html encoding + whitesapce from client state
    # html_parser = HTMLParser.HTMLParser()
    # client_state = html_parser.unescape(client_state)
    # client_state = "".join(client_state.split())

    #poll the database
	while question == None:
   		time.sleep(0.2)
    # data = get_data()
    # json_state = to_json(data)
    # json_state = "".join(data) #remove whitespace
  	data = question
   	question = None
   	print "q polling:", data
   	return data

@website.route('/answer_poll')
def answerPoll():
	global answer
	#remove html encoding + whitesapce from client state
    # html_parser = HTMLParser.HTMLParser()
    # client_state = html_parser.unescape(client_state)
    # client_state = "".join(client_state.split())

    #poll the database
	while answer == None:
   		time.sleep(0.2)
    # data = get_data()
    # json_state = to_json(data)
    # json_state = "".join(data) #remove whitespace
  	data = answer
   	answer = None
   	print "a polling:", data
   	return data

def setQuestion(s):
	global question
	print "question:", s
	question = s

def setAnswer(s):
	global answer
	print "answer:", s
	answer = s