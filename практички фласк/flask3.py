#практичка фласк 3, вариант 4
from flask import Flask

app = Flask(__name__)

@app.route('/post/<string:slug>')
def show_post(slug):
    return f"Пост: {slug}"

if __name__ == '__main__':
    app.run(debug=True)