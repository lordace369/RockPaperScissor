from flask import Flask,render_template,request
import random



app=Flask(__name__)

def game(you,comp):
    result=''
    if you==comp:
        result= 'draw ho gya'
    elif you=='paper' and comp=='rock':
        result= 'you win'
    elif you=='rock' and comp=='scissor':
        result= 'you win'
    elif you=='scissor' and comp=='paper':
        result= 'you win'
    else:
        result='you lose'
    return result


@app.route('/',methods=['GET','POST'])
def index():
    choice=''
    compChoice=''
    verdict=''
    options=['rock','paper','scissor']
    if request.method=='POST' and 'choice' in request.form:
        compChoice=random.choice(options)
        if request.form.get('choice').lower() in options:
            choice=request.form.get('choice').lower()
            verdict=game(choice,compChoice)
    return render_template('index.html',choice=choice,compChoice=compChoice,verdict=verdict)



if __name__=='__main__':
    app.run(debug=True)