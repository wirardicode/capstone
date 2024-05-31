from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os
import re

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files: #file tdk ditemukan
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '': #file ditemuka tanpa nama/tidak mengirim gambar
        return jsonify({"error": "No selected file"}), 400

    if file: #file ditemukan    
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)

        #mencari fotal harga barang = xxxx
        #---------------------------------
        #fotal_harga = None
        #jumlah =None
        #for line in text.splitlines():
         #   if "Fotal harga:" in line:
          #      fotal_harga = line.strip()
        
        # Mengembalikan output 'Fotal harga: xxx'
        #if fotal_harga:
         #   return jsonify({"text": fotal_harga})
        #else:
         #   return jsonify({"error": "fotal isnot found"}), 404
        #---------------------------------

         # Mencari teks 'Fotal harga: xxx'
         #------------------------------------
        # Mencari angka di baris terakhir
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        last_line = None
        for line in reversed(lines):
            if any(char.isdigit() for char in line):
                last_line = line
                break

        # Mengembalikan output angka di baris terakhir
        if last_line:
            return jsonify({"Money spend": last_line})
        else:
            return jsonify({"error": "Number not found sorry"}), 404
        #--------------------------------------------

        #return jsonify({"text": text}) # jangan hapus tanda koment ini soalnya baut uji output teks keseluruhan <ekstrasi semua teks> 

    return jsonify({"error": "File processing error"}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)  
    print("app is running")
