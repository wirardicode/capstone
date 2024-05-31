# Menggunakan image dasar Python
FROM python:3

# Set working directory
WORKDIR /app

# Menyalin file requirements dan menginstal dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Menyalin seluruh kode aplikasi ke dalam container
COPY . .

# Menjalankan aplikasi
CMD ["python", "main.py", "app"]  # Anda bisa menyesuaikan perintah ini sesuai dengan entry point aplikasi Anda
