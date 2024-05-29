# image python 3
FROM python:3

# Set direktori kerja di dalam container
WORKDIR /app

# Salin dependencies file dan instal dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi ke dalam container
COPY ocrApi.py .

# Jalankan aplikasi saat container dijalankan
CMD ["python", "ocrApi.py"]
