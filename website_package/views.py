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
@website.route('/')
def index():
	question = "Compare Bose headphones to a Macbook Pro"
	answer = "A Bose SoundTrue around-ear headphones II is worth 0.07 Apple 13"
<<<<<<< HEAD
	return render_template('website/index.html',title='Worth It?',question=question,answer=answer)
=======
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
   	# print "polling:", json.dumps({"data": answer})
   	return json.dumps({"data": data})

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
   	# print "polling:", json.dumps({"data": answer})
   	return json.dumps({"data": data})
>>>>>>> 0ea62121ce56f62b1baee2eab4cef6646c73a8d4

def setQuestion(s):
	global question
	print "question:", s
	question = s

def setAnswer(s):
	global answer
	print "answer:", s
	answer = s