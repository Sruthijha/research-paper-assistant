import fitz

def extract_text_with_pages(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    data = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        data.append({
            "page": page_num + 1,
            "text": text
        })

    return data


def chunk_text_with_pages(pages, chunk_size=1000, overlap=200):
    chunks = []

    for page in pages:
        text = page["text"]
        page_num = page["page"]

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "page": page_num
            })

            start += chunk_size - overlap

    return chunks