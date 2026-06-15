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

    return {
        "contract_name": contract_name,
        "lines_of_code": lines_of_code
    }