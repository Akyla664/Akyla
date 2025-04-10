#практичка фласк 1, вариант 4
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    
    return f'Имя пользователя: {username}'

if __name__ == '__main__':
    app.run(debug=True)