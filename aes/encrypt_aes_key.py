from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes
import os

# قراءة المفتاح العام
with open("keys/public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# قراءة AES key
with open("encrypted/aes_key.bin", "rb") as f:
    aes_key = f.read()

# تشفير مفتاح AES باستخدام RSA
encrypted_key = public_key.encrypt(
    aes_key,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# حفظ المفتاح المشفّر
with open("encrypted/encrypted_aes_key.bin", "wb") as f:
    f.write(encrypted_key)