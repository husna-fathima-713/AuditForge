from flask import Flask, render_template, request
from src.analyzer import analyze_contract
import os

app = Flask(__name__)

UPLOAD_FOLDER = "contracts"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("contract")

    if not file:
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    result = analyze_contract(filepath)

    return f"""
    Contract Name: {result['contract_name']}<br>
    Lines of Code: {result['lines_of_code']}<br>
    File Name: {file.filename}<br>
    Solidity Version: {result['solidity_version']}<br>
    External Calls: {result['external_calls']}<br>
    Reentrancy Risk: {result['reentrancy_risk']}
    """

if __name__ == "__main__":
    app.run(debug=True)