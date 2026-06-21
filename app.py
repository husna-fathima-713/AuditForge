from flask import Flask, render_template, request
from src.analyzer import analyze_contract
from src.report_generator import generate_report
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

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    result = analyze_contract(filepath)

    generate_report(result)

    return render_template(
        "report.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)