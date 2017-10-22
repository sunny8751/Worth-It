import os
from website_package import website
import website_package
from alexa_package import alexa


from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event

from website_package.views import setQuestion, getQuestion, setAnswer, getAnswer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.register_blueprint(website)
app.register_blueprint(alexa)
# app.run(threaded=True)

#turn the flask app into a socketio app
socketio = SocketIO(app)

thread1 = Thread()
thread2 = Thread()

thread_stop_event = Event()

class QuestionThread(Thread):
    def __init__(self):
        self.delay = .2
        super(QuestionThread, self).__init__()

    def updateQuestion(self):
        print "Waiting for question"
        while not thread_stop_event.isSet():
            while getQuestion() == None:
            	sleep(self.delay)
            print("question:", getQuestion())
            socketio.emit('question', {'question': getQuestion()}, namespace='/test')
            setQuestion(None)

    def run(self):
    	self.updateQuestion()

class AnswerThread(Thread):
    def __init__(self):
        self.delay = .2
        super(AnswerThread, self).__init__()

    def updateAnswer(self):
        print "Waiting for answer"
        while not thread_stop_event.isSet():
            while getAnswer() == None:
            	sleep(self.delay)
            print("answer:", getAnswer())
            socketio.emit('answer', {'answer': getAnswer()}, namespace='/test')
            setAnswer(None)

    def run(self):
    	self.updateAnswer()

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread1
    global thread2
    # global thread2
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread1.isAlive():
        print "Starting Thread1"
        thread1 = QuestionThread()
        thread1.start()

    if not thread2.isAlive():
        print "Starting Thread1"
        thread2 = AnswerThread()
        thread2.start()

    # if not thread2.isAlive():
    #     print "Starting Thread2"
    #     thread2 = website_package.views.AnswerThread()
    #     thread2.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



# debug=True, 


if __name__ == '__main__':
    socketio.run(app)
