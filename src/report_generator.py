from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_report(result):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    contract_name = result["contract_name"]

    txt_filename = (
        f"reports/{contract_name}_{timestamp}.txt"
    )

    report_content = f"""
=============================
      AUDITFORGE REPORT
=============================

Contract Name: {result['contract_name']}
Lines of Code: {result['lines_of_code']}
Solidity Version: {result['solidity_version']}

Overall Risk Level: {result['risk_level']}

-----------------------------
FINDING SUMMARY
-----------------------------

Total Findings: {result['total_findings']}
High Severity: {result['high_count']}
Medium Severity: {result['medium_count']}
Low Severity: {result['low_count']}
"""

    if result["reentrancy_finding"]:

        report_content += f"""

REENTRANCY FINDING

Severity: {result['reentrancy_finding']['severity']}
Issue: {result['reentrancy_finding']['title']}
Reason: {result['reentrancy_finding']['reason']}
"""

    if result["overflow_finding"]:

        report_content += f"""

OVERFLOW FINDING

Severity: {result['overflow_finding']['severity']}
Issue: {result['overflow_finding']['title']}
Reason: {result['overflow_finding']['reason']}
"""

    if result["access_control_finding"]:

        report_content += f"""

ACCESS CONTROL FINDING

Severity: {result['access_control_finding']['severity']}
Issue: {result['access_control_finding']['title']}
Reason: {result['access_control_finding']['reason']}
"""

    with open(
        txt_filename,
        "w",
        encoding="utf-8"
    ) as report_file:

        report_file.write(report_content)

    generate_pdf_report(
        result,
        contract_name,
        timestamp
    )


def generate_pdf_report(
    result,
    contract_name,
    timestamp
):

    pdf_filename = (
        f"reports/{contract_name}_{timestamp}.pdf"
    )

    pdf = SimpleDocTemplate(
        pdf_filename
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AuditForge Security Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"Contract Name: {result['contract_name']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Lines of Code: {result['lines_of_code']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Solidity Version: {result['solidity_version']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Risk Level: {result['risk_level']}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "Finding Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Findings: {result['total_findings']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"High Severity: {result['high_count']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Medium Severity: {result['medium_count']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Low Severity: {result['low_count']}",
            styles["BodyText"]
        )
    )

    pdf.build(elements)