from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API on Render.com working!"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == '__main__':
    app.run()
