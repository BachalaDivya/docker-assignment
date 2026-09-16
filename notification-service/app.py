from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Notification Service",
        "status": "running"
    })

@app.route('/notify')
def notify():
    return jsonify({
        "message": "Notification sent successfully"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
