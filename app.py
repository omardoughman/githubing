from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def data():
    return jsonify({
        "message": "Hello from Python API",
        "status": "ok"
    })

app.run(host="0.0.0.0", port=5000)
