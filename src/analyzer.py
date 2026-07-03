import re

from src.parser import parse_contract

from src.reentrancy import (
    detect_external_calls,
    detect_reentrancy_risk
)

from src.detectors.reentrancy_detector import ReentrancyDetector
from src.detectors.overflow_detector import OverflowDetector
from src.detectors.access_control_detector import AccessControlDetector


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

    detectors = [
        ReentrancyDetector(),
        OverflowDetector(),
        AccessControlDetector()
    ]

    findings = []

    for detector in detectors:

        finding = detector.analyze(code)

        if finding:
            findings.append(finding)

    reentrancy_finding = None
    overflow_finding = None
    access_control_finding = None

    for finding in findings:

        if finding["title"] == "Potential Reentrancy Vulnerability":
            reentrancy_finding = finding

        elif finding["title"] == "Potential Integer Overflow":
            overflow_finding = finding

        elif finding["title"] == "Missing Access Control":
            access_control_finding = finding

    high_count = sum(
        1 for f in findings
        if f["severity"] == "HIGH"
    )

    medium_count = sum(
        1 for f in findings
        if f["severity"] == "MEDIUM"
    )

    low_count = sum(
        1 for f in findings
        if f["severity"] == "LOW"
    )

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

        "state_variables": parsed["state_variables"],

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