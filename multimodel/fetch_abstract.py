import PyPDF2
import requests


def fetch_abstract(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    return data["message"].get("abstract", "No abstract found")  # type: ignore


def extract_text_from_pdf(pdf_path):
    text= ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text+= page.extract_text() or ""   
    return text
