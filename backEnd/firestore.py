from google.cloud import firestore

# Inisialisasi Firestore
db = firestore.Client()

def add_data(collection_name, data):
    doc_ref = db.collection(collection_name).add(data)
    return doc_ref

def get_data(collection_name):
    docs = db.collection(collection_name).stream()
    return [doc.to_dict() for doc in docs]

# Contoh penggunaan
if __name__ == '__main__':
    # Menambahkan data ke Firestore
    data = {"name": "example", "value": 123}
    add_data("example_collection", data)
    
    # Mendapatkan data dari Firestore
    data = get_data("example_collection")
    print(data)
