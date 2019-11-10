#

from flask import Flask, send_file, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return jsonify({"status": "ok"})


@app.route("/api")
def test_again():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)  # stops here
    print("Server died")
