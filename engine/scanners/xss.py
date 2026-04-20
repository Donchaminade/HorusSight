from engine.utils.requester import send_request

PAYLOAD = "<script>alert(1)</script>"

def scan_xss(url):
    findings = []

    test_url = f"{url}?q={PAYLOAD}"
    response = send_request(test_url)

    if response and PAYLOAD in response.text:
        findings.append({
            "type": "XSS",
            "url": url,
            "payload": PAYLOAD,
            "evidence": "Payload reflected in response"
        })

    return findings
