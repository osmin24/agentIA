import chromadb
client = chromadb.Client()
collection = client.create_collection("test")
collection.add(documents=["test doc"], ids=["1"])
try:
    results = collection.query(query_texts=["test"], where=None)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
