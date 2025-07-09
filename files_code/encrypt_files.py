import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# الملفات الأصلية
input_files = {
    "fake_data": "test_data/fake_data.json",
    "fake_message": "test_data/fake_message.txt"
}

# مجلد الإخراج
output_dir = "encrypted"
os.makedirs(output_dir, exist_ok=True)

# توليد مفتاح AES و IV
aes_key = os.urandom(32)
iv = os.urandom(16)

# حفظ المفتاح و IV
with open(f"{output_dir}/aes_key.bin", "wb") as f:
    f.write(aes_key)
with open(f"{output_dir}/iv.bin", "wb") as f:
    f.write(iv)

# دالة التشفير
def encrypt_file(input_path, output_path, key, iv):
    with open(input_path, "rb") as f:
        plaintext = f.read()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encrypted = cipher.encryptor().update(padded) + cipher.encryptor().finalize()
    with open(output_path, "wb") as f:
        f.write(encrypted)

# تطبيق التشفير على الملفات
for name, path in input_files.items():
    encrypt_file(path, f"{output_dir}/{name}.enc", aes_key, iv)