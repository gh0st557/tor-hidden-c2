import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    # Logika do analizy lub wydawania poleceń agentowi
    return {"status": "received", "command": "standby"}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
