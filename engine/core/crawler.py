import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(base_url):
    visited = set()
    to_visit = [base_url]
    discovered = []

    while to_visit:
        url = to_visit.pop()

        if url in visited:
            continue

        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            discovered.append(url)

            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                full_url = urljoin(base_url, link["href"])

                if full_url not in visited:
                    to_visit.append(full_url)

        except:
            continue

    return list(set(discovered))
