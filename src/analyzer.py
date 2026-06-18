from src.reentrancy import (
    detect_external_calls,
    detect_reentrancy_risk,
    generate_reentrancy_finding
)

from src.overflow import generate_overflow_finding

from src.access_control import generate_access_control_finding

import re


def analyze_contract(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    lines_of_code = len(code.splitlines())

    contract_match = re.search(
        r"contract\s+(\w+)",
        code
    )

    contract_name = (
        contract_match.group(1)
        if contract_match
        else "Unknown"
    )

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

    if reentrancy_finding or access_control_finding:
        risk_level = "HIGH"

    elif overflow_finding:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "contract_name": contract_name,
        "lines_of_code": lines_of_code,
        "solidity_version": solidity_version,
        "external_calls": external_calls,
        "reentrancy_risk": reentrancy_risk,
        "risk_level": risk_level,
        "reentrancy_finding": reentrancy_finding,
        "overflow_finding": overflow_finding,
        "access_control_finding": access_control_finding
    }