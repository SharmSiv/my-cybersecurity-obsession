from flask import Flask, render_template, request, jsonify
from checker.strength import PasswordAnalyzer
import os

app = Flask(__name__)
checker = PasswordAnalyzer()

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    
    result = checker.check(password)
    return jsonify(result)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )