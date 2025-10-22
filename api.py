# api.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/data')
def data():
    return jsonify({"message": "Hello API!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
