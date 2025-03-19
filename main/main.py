from flask import Flask, render_template, request, jsonify
from support.password import create_password

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', method=['POST'])
def generate():
    data = request.json
    user_request = data.get('message')
    password = create_password(user_request)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)