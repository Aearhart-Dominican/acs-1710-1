from flask import Flask

import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def dessert(users_dessert):
    return f'How did you know i liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'Marketing tactics work too well on me. Just yesterday I went in the grocery store for milk and walked out with a {adjective} {noun}!'

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    if num1.isdigit() and num2.isdigit():
        total = int(num1) * int(num2)
        string = f'{num1} * {num2} = {total}'
    else:
        string ='Invalid Inputs: Try again with two numbers'
    return string
        
@app.route('/sayntimes/<text>/<num>')
def sayntimes(text, num):
    string = ""
    if num.isdigit():
        for i in range(int(num)):
            string +=  text + " "
    else:
        string = "Invalid Input: Use a number as your second input"
    return string

@app.route('/dicegame')
def dicegame():
    num = random.randint(1,6)
    if num == 6:
        string = f'You rolled a {num}. You won!'
    else:
        string = f'You rolled a {num}. You lost!'

    return string

if __name__ == '__main__':
    app.run(debug=True)