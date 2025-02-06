from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/message", methods=["POST"])
def receive_message():
    data = request.get_json()
    message = (data["message"])
    print("msg reçu : " + message)
    return jsonify({"response": f"Msg reçu: {message}"}), 200

app.run(host="0.0.0.0", port=5007)