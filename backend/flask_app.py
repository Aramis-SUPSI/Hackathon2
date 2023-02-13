from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/prova1')
def prova1():
    return jsonify('Hello, World!')

if __name__ == '__main__':
    app.run(port=8000)
