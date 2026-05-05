from flask import Flask, request, jsonify

app = Flask(__name__)

ADMIN_EMAIL = "omardoughman52@gmail.com"
ADMIN_TOKEN = "OMAR-DASH-52-ACCESS-KEY"

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data["email"] == ADMIN_EMAIL and data["token"] == ADMIN_TOKEN:
        return jsonify({"ok": True})

    return jsonify({"ok": False}), 403

@app.route("/data")
def data():
    return {"message": "secure data unlocked"}

if __name__ == "__main__":
    app.run(port=5000)
