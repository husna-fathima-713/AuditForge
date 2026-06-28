import re


def parse_contract(code):

    contract_match = re.search(
        r"contract\s+(\w+)",
        code
    )

    contract_name = (
        contract_match.group(1)
        if contract_match
        else "Unknown"
    )

    function_pattern = (
        r"function\s+(\w+)\s*\("
    )

    functions = re.findall(
        function_pattern,
        code
    )

    mapping_pattern = (
        r"mapping\s*\([^)]*\)\s*(?:public|private|internal)?\s*(\w+)"
    )

    mappings = re.findall(
        mapping_pattern,
        code
    )

    return {

        "contract_name": contract_name,

        "functions": functions,

        "mappings": mappings
    }