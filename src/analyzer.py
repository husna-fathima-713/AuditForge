from src.reentrancy import (
    detect_external_calls,
    detect_reentrancy_risk,
    generate_reentrancy_finding
)

from src.overflow import generate_overflow_finding
from src.access_control import generate_access_control_finding
from src.parser import parse_contract

import re


def analyze_contract(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    parsed = parse_contract(code)

    lines_of_code = len(code.splitlines())

    pragma_match = re.search(
        r"pragma\s+solidity\s+([^;]+);",
        code
    )

    solidity_version = (
        pragma_match.group(1)
        if pragma_match
        else "Unknown"
    )

    external_calls = detect_external_calls(code)

    reentrancy_risk = detect_reentrancy_risk(code)

    reentrancy_finding = generate_reentrancy_finding(code)

    overflow_finding = generate_overflow_finding(code)

    access_control_finding = generate_access_control_finding(code)

    findings = [
        reentrancy_finding,
        overflow_finding,
        access_control_finding
    ]

    findings = [f for f in findings if f]

    high_count = 0
    medium_count = 0
    low_count = 0

    for finding in findings:

        if finding["severity"] == "HIGH":
            high_count += 1

        elif finding["severity"] == "MEDIUM":
            medium_count += 1

        elif finding["severity"] == "LOW":
            low_count += 1

    total_findings = len(findings)

    if high_count > 0:
        risk_level = "HIGH"
    elif medium_count > 0:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {

        "contract_name": parsed["contract_name"],

        "functions": parsed["functions"],

        "mappings": parsed["mappings"],

        "lines_of_code": lines_of_code,

        "solidity_version": solidity_version,

        "external_calls": external_calls,

        "reentrancy_risk": reentrancy_risk,

        "risk_level": risk_level,

        "reentrancy_finding": reentrancy_finding,

        "overflow_finding": overflow_finding,

        "access_control_finding": access_control_finding,

        "total_findings": total_findings,

        "high_count": high_count,

        "medium_count": medium_count,

        "low_count": low_count
    }