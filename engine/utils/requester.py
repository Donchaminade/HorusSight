import requests

def send_request(url, method="GET"):
    try:
        if method == "GET":
            return requests.get(url, timeout=5)
        else:
            return requests.post(url, timeout=5)
    except Exception:
        return None
