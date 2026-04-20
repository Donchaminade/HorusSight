from engine.core.crawler import crawl
from engine.scanners.sqli import scan_sqli
from engine.scanners.xss import scan_xss

def run_scan(target_url):
    urls = crawl(target_url)

    all_findings = []

    for url in urls:
        all_findings.extend(scan_sqli(url))
        all_findings.extend(scan_xss(url))

    return {
        "target": target_url,
        "vulnerabilities": all_findings
    }
