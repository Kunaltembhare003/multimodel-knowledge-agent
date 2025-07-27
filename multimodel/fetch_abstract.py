import requests


def fetch_abstract(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    return data["message"].get("abstract", "No abstract found") # type: ignore
