from flask import Flask, render_template, request
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

    return f"Contract saved successfully: {file.filename}"

if __name__ == "__main__":
    app.run(debug=True)