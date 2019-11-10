from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def send_js():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="localhost", port=3001, debug=True)  # stops here
    print("Server died")
