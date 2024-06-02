import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore DB
cred = credentials.Certificate(r'D:\koding\kode utama\capstone\backEnd\config\service.json')
firebase_admin.initialize_app(cred)

db = firestore.client() #koneksi ke firestore default

def save_to_firestore(data):
    try:
        # Menyimpan data ke Firestore
        db.collection('ocr_results').add(data)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
