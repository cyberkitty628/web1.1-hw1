from flask import Flask

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
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """Display a funny story to the user depending on what adjective/noun they enter."""
    return f'Today, I met a {adjective} cat standing on her hind legs. She offered me a {noun} and disappeared into the shadows.'

@app.route('/multiply/<number1>/number2>')
def multiply(number1, number2):
    """Multiply numbers entered by user."""
    if number1.isdigit() and number2.isdigit():
        answer = int(number1) * int(number2)
        return f'{number1} times {number2} equals {answer}!'
    else:
        return f'Invalid inputs. Please try again by entering two numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Displays user word a certain number of times based on user inputs."""
    if str(word) and int(n):
        repeat = str(word) * int(n)
        return repeat
    else:
        return f'Invalid input. Please try again by entering a word and a number!'

if __name__ == '__main__':
    app.run(debug=True)