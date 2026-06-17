def detect_external_calls(code):

    findings = []

    if ".call" in code:
        findings.append("call() detected")

    if ".transfer(" in code:
        findings.append("transfer() detected")

    if ".send(" in code:
        findings.append("send() detected")

    return findings


def detect_reentrancy_risk(code):

    dangerous_patterns = [
        ".call",
        ".transfer(",
        ".send("
    ]

    for pattern in dangerous_patterns:
        if pattern in code:
            return True

    return False


def generate_reentrancy_finding(code):

    if detect_reentrancy_risk(code):

        return {
            "severity": "HIGH",
            "title": "Potential Reentrancy Vulnerability",
            "reason": "External call detected in contract."
        }

    return None