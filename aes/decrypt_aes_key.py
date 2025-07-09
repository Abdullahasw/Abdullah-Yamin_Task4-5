from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes


password = b"PrivkeyPassword"
# قراءة المفتاح الخاص المحمي بكلمة مرور
with open("keys/private_key_secure.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=password
    )
# قراءة المفتاح المشفّر
with open("encrypted/encrypted_aes_key.bin", "rb") as f:
    encrypted_key = f.read()

# فك تشفير مفتاح AES
decrypted_aes_key = private_key.decrypt(
    encrypted_key,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# حفظ المفتاح المفكوك (اختياري)
with open("decrypted/decrypted_aes_key.bin", "wb") as f:
    f.write(decrypted_aes_key)