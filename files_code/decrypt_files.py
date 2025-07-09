import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# إعداد المسارات
input_files = {
    "fake_data": "encrypted/fake_data.enc",
    "fake_message": "encrypted/fake_message.enc"
}
output_dir = "decrypted"
os.makedirs(output_dir, exist_ok=True)

# قراءة مفتاح AES و IV من الملفات
with open("decrypted\decrypted_aes_key.bin", "rb") as f:
    aes_key = f.read()

with open("encrypted/iv.bin", "rb") as f:
    iv = f.read()

# دالة لفك التشفير
def decrypt_file(input_path, output_path, key, iv):
    with open(input_path, "rb") as f:
        ciphertext = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # إزالة الـ padding
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(data)

# فك التشفير لجميع الملفات
for name, path in input_files.items():
    output_path = os.path.join(output_dir, f"{name}.txt")  # .txt فقط لسهولة الفتح
    decrypt_file(path, output_path, aes_key, iv)