from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)
        return jsonify({"text": text})

    return jsonify({"error": "File processing error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)  
    print("app is running")
