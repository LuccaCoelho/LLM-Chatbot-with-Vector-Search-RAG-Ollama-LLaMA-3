import pandas as pd

def chunk_text(text, chunk_size=500, overlap=100):
    chunk_list = []

    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunk_list.append({"chunk_id": chunk_id, "text": chunk})
            chunk_id += 1

            start += chunk_size - overlap

    df = pd.DataFrame(chunk_list)

    return df