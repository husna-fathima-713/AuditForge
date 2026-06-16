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