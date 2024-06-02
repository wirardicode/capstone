from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from waitress import serve
import os
import re
from firestore import save_to_firestore  # Import fungsi dari firestore.py
from storages import upload_to_storage  # Import fungsi dari storages.py

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:  # file tdk ditemukan
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '':  # file ditemukan tanpa nama/tidak mengirim gambar
        return jsonify({"error": "No selected file"}), 400

    if file:  # file ditemukan
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)

        # Mencari angka di baris terakhir
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        last_line = None
        for line in reversed(lines):
            if any(char.isdigit() for char in line):
                last_line = line
                break

        # Mengunggah file ke Cloud Storage
        file.stream.seek(0)  # Reset stream position to the beginning
        file_url = upload_to_storage(file.stream, file.filename)

        # Mengembalikan output angka di baris terakhir
        if last_line:
            result = {"Money spend": last_line, "image_url": file_url}
            # Simpan hasil ke Firestore
            save_to_firestore(result)
            return jsonify(result)
        else:
            return jsonify({"error": "Number not found sorry"}), 404

    return jsonify({"error": "File processing error"}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=3000)
