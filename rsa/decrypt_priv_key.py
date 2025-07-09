from cryptography.hazmat.primitives import serialization

# كلمة المرور التي تم استخدامها عند التشفير
password = b"PrivkeyPxdassword"  # you could change it

# قراءة المفتاح الخاص المحمي بكلمة مرور
with open("keys/private_key_secure.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=password
    )
