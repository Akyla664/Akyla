#практичка фласк 2, вариант 4
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'  


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('Нет части файла в запросе')
            return redirect(request.url)
        
        file = request.files['file']
        
        
        if file.filename == '':
            flash('Файл не выбран')
            return redirect(request.url)
        
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Файл успешно загружен')
            return redirect(url_for('upload_file'))
        else:
            flash('Недопустимый тип файла. Разрешены только JPG и PNG.')
            return redirect(request.url)
    
    return render_template('index.html')

if __name__ == '__main__':
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)