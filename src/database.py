import sqlite3


def initialize_database():

    connection = sqlite3.connect(
        "auditforge.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audits (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            contract_name TEXT,

            risk_level TEXT,

            total_findings INTEGER,

            scan_time TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_audit(
    contract_name,
    risk_level,
    total_findings,
    scan_time
):

    connection = sqlite3.connect(
        "auditforge.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO audits
        (
            contract_name,
            risk_level,
            total_findings,
            scan_time
        )

        VALUES (?, ?, ?, ?)
    """,
    (
        contract_name,
        risk_level,
        total_findings,
        scan_time
    ))

    connection.commit()
    connection.close()


def get_all_audits():

    connection = sqlite3.connect(
        "auditforge.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM audits
        ORDER BY id DESC
    """)

    audits = cursor.fetchall()

    connection.close()

    return audits


def get_dashboard_stats():

    connection = sqlite3.connect(
        "auditforge.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM audits"
    )

    total_audits = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM audits WHERE risk_level='HIGH'"
    )

    high_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM audits WHERE risk_level='MEDIUM'"
    )

    medium_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM audits WHERE risk_level='LOW'"
    )

    low_count = cursor.fetchone()[0]

    connection.close()

    return {
        "total_audits": total_audits,
        "high_count": high_count,
        "medium_count": medium_count,
        "low_count": low_count
    }