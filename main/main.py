from flask import Flask, render_template, request, jsonify
from support.password import create_password

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length'))
    uppercase = data.get('uppercase')
    lowercase = data.get('lowercase')
    numbers = data.get('numbers')
    symbols = data.get('symbols')
    password = create_password(length, uppercase, lowercase, numbers, symbols)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run()