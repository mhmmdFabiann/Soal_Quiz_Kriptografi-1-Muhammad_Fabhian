from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

from vigenere import encrypt_vigenere, decrypt_vigenere
from playfair import encrypt_playfair, decrypt_playfair
from hill import encrypt_hill, decrypt_hill

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        text = request.form.get('text')
        key = request.form.get('key')
        cipher_type = request.form.get('cipher')
        action = request.form.get('action')

        if not key or len(key) < 12:
            return "Kunci harus minimal 12 karakter", 400

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            message = read_file_content(file_path)
        else:
            message = text

        if cipher_type == 'vigenere':
            if action == 'encrypt':
                result = encrypt_vigenere(message, key)
            else:
                result = decrypt_vigenere(message, key)
        elif cipher_type == 'playfair':
            if action == 'encrypt':
                result = encrypt_playfair(message, key)
            else:
                result = decrypt_playfair(message, key)
        elif cipher_type == 'hill':
            if action == 'encrypt':
                result = encrypt_hill(message, key)
            else:
                result = decrypt_hill(message, key)
        else:
            result = "Invalid cipher type"

        return render_template('result.html', result=result)

    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
