from flask import Flask, render_template,url_for, request, redirect, Markup,flash
import os
import datetime

app = Flask(__name__)

begin_time = None
solved = False

@app.route('/', methods=['GET'])
def main_page():
    global begin_time
    global solved
    if begin_time == None:
        return render_template('start.html')
    elif not solved:
        return render_template('challenge.html')
    # TODO ADD IF TIME IS UP, RENDER GAME OVER
    else:
        return render_template('end.html')
    
@app.route('/begin', methods=['GET'])
def begin():
    global begin_time 
    print("Let's begin !")
    if begin_time == None:
        begin_time = datetime.datetime.now()
    return redirect(url_for('main_page'))

@app.route('/solve', methods=['POST'])
def solve():
    global solved
    pin = request.form['pin']
    print('Try to solve with ', pin)
    # TODO ADD TIME UP CHECK
    if (pin == "2906"):
        solved = True
    return redirect(url_for('main_page'))

if __name__ =='__main__': 
    app.run(debug=True) 
