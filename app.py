from flask import Flask, render_template,url_for, request, redirect, Markup,flash
import os

app = Flask(__name__)

@app.route('/', methods =   ['GET'])
def index0():
    print("method index0")
    return render_template('index0.html')
    
@app.route('/index1.html', methods =   ['POST','GET'])
def index1():
    print("method index")
    if request.method == 'POST' :
        task_content = request.form['content']
        print(task_content)
        print("task?")
        if (task_content == "2906") :
            return render_template("meta.html")
        else :
            message = Markup("<h1>Voila! test_message is ready to used</h1>")
            print(message)
    
        
    
    print("Entered render template index.html")
    return render_template('index1.html')




if __name__ =='__main__': 
    app.run(debug=True) 
