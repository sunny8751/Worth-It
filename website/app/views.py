from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	question = "Compare Bose headphones to a Macbook Pro"
	answer = "A Bose SoundTrue around-ear headphones II is worth 0.07 Apple 13"
   	return render_template('index.html',title='Worth It?',question=question,answer=answer)