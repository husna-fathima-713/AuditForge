from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from src.auth import (
    get_user,
    verify_login
)

from src.analyzer import analyze_contract
from src.report_generator import generate_report

from src.database import (
    initialize_database,
    save_audit,
    get_all_audits,
    get_dashboard_stats
)

from datetime import datetime

import os

app = Flask(__name__)

app.secret_key = "auditforge_secret_key"

UPLOAD_FOLDER = "contracts"

initialize_database()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if verify_login(username, password):

            user = get_user(username)

            login_user(user)

            return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template(
        "login.html",
        error=None
    )


@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))


@app.route("/")
@login_required
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
@login_required
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

    save_audit(
        result["contract_name"],
        result["risk_level"],
        result["total_findings"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    return render_template(
        "report.html",
        result=result
    )


@app.route("/history")
@login_required
def history():

    audits = get_all_audits()

    stats = get_dashboard_stats()

    return render_template(
        "history.html",
        audits=audits,
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)