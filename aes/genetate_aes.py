import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# generate random AES (256 bit = 32 byte) توليد مفتاح AES عشوائي (256 بت = 32 بايت)
aes_key = os.urandom(32)

# generate random IV (128 bit = 16 byte) توليد IV عشوائي (128 بت = 16 بايت)
iv = os.urandom(16)

# creat output folder إنشاء مجلد الإخراج
os.makedirs("encrypted", exist_ok=True)

# حفظ المفتاح و IV في ملفات
with open("encrypted/aes_key.bin", "wb") as f:
    f.write(aes_key)

with open("encrypted/iv.bin", "wb") as f:
    f.write(iv)

# # مثال: بيانات بسيطة نريد تشفيرها (في حال ما في ملف جاهز)
# plaintext = b"This is a test message for AES CBC mode encryption."

# # عمل padding للبيانات
# padder = padding.PKCS7(128).padder()
# padded_data = padder.update(plaintext) + padder.finalize()

# استخدام AES CBC للتشفير
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
# ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# حفظ البيانات المشفرة
# with open("encrypted/test_data.enc", "wb") as f:
#     f.write(ciphertext)