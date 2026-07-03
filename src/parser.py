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
        r"function\s+(\w+)\s*\((.*?)\)\s*([^{]*)"
    )

    functions = []

    for match in re.finditer(function_pattern, code, re.DOTALL):

        name = match.group(1)

        parameters = match.group(2).strip()

        declaration = match.group(3)

        visibility = "default"

        for keyword in [
            "public",
            "private",
            "external",
            "internal"
        ]:

            if keyword in declaration:
                visibility = keyword
                break

        modifiers = []

        tokens = declaration.split()

        ignore = {
            "public",
            "private",
            "external",
            "internal",
            "view",
            "pure",
            "payable",
            "virtual",
            "override",
            "returns"
        }

        for token in tokens:

            token = token.strip()

            if token not in ignore:

                if "(" not in token:

                    modifiers.append(token)

        functions.append({

            "name": name,

            "parameters": parameters,

            "visibility": visibility,

            "modifiers": modifiers

        })

    mapping_pattern = (
        r"mapping\s*\([^)]*\)\s*(?:public|private|internal)?\s*(\w+)"
    )

    mappings = re.findall(
        mapping_pattern,
        code
    )

    state_variable_pattern = (
        r"(?:uint|int|bool|address|string|bytes\d*|bytes)\s+(?:public|private|internal)?\s*(\w+)"
    )

    state_variables = re.findall(
        state_variable_pattern,
        code
    )

    return {

        "contract_name": contract_name,

        "functions": functions,

        "mappings": mappings,

        "state_variables": state_variables

    }