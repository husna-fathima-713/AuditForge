import re

def detect_overflow_risk(code):

    old_version = False

    pragma_match = re.search(
        r"pragma\s+solidity\s+\^?(\d+)\.(\d+)\.(\d+)",
        code
    )

    if pragma_match:

        major = int(pragma_match.group(1))
        minor = int(pragma_match.group(2))

        if major == 0 and minor < 8:
            old_version = True

    arithmetic_found = (
        "+" in code or
        "-" in code or
        "*" in code
    )

    return old_version and arithmetic_found


def generate_overflow_finding(code):

    if detect_overflow_risk(code):

        return {
            "severity": "MEDIUM",
            "title": "Potential Integer Overflow",
            "reason": "Arithmetic operations found in Solidity version below 0.8.0."
        }

    return None