from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    chars = ""
    if 'upper' in request.form:
        chars += string.ascii_uppercase
    if 'lower' in request.form:
        chars += string.ascii_lowercase
    if 'number' in request.form:
        chars += string.digits
    if 'symbol' in request.form:
        chars += string.punctuation

    if not chars:
        return jsonify({'error': 'Please select at least one character set.'})

    password = ''.join(random.choice(chars) for _ in range(length))
    return jsonify({'password': password})

if __name__ == "__main__":
    app.run(debug=True)
