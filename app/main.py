from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from version Gule Gule K8s2!deneme_4"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
