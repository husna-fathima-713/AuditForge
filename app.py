from flask import (
    Flask,
    render_template,
    request
)

from src.analyzer import analyze_contract
from src.report_generator import generate_report

from src.database import (
    initialize_database,
    save_audit,
    get_all_audits
)

from datetime import datetime

import os

app = Flask(__name__)

UPLOAD_FOLDER = "contracts"

initialize_database()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get(
        "contract"
    )

    if not file:
        return "No file selected"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    result = analyze_contract(
        filepath
    )

    generate_report(result)

    save_audit(
        result["contract_name"],
        result["risk_level"],
        result["total_findings"],
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    return render_template(
        "report.html",
        result=result
    )


@app.route("/history")
def history():

    audits = get_all_audits()

    return render_template(
        "history.html",
        audits=audits
    )


if __name__ == "__main__":
    app.run(debug=True)