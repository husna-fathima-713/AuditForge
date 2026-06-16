from src.reentrancy import detect_external_calls
import re

def analyze_contract(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    lines_of_code = len(code.splitlines())

    contract_match = re.search(r"contract\s+(\w+)", code)

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

    return {
        "contract_name": contract_name,
        "lines_of_code": lines_of_code,
        "solidity_version": solidity_version,
        "external_calls": external_calls
    }