def generate_access_control_finding(code):

    sensitive_functions = [
        "mint",
        "burn",
        "withdraw",
        "pause",
        "transferOwnership"
    ]

    ownership_checks = [
        "onlyOwner",
        "msg.sender == owner"
    ]

    found_sensitive = False

    for function_name in sensitive_functions:
        if function_name in code:
            found_sensitive = True
            break

    protected = False

    for check in ownership_checks:
        if check in code:
            protected = True
            break

    if found_sensitive and not protected:

        return {
            "severity": "HIGH",
            "title": "Missing Access Control",
            "reason": "Sensitive functionality detected without ownership validation."
        }

    return None