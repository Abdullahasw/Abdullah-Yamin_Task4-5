import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# إنشاء مجلد keys إذا ما كان موجود
os.makedirs("keys", exist_ok=True)

# توليد مفتاح خاص RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# توليد المفتاح العام من الخاص
public_key = private_key.public_key()

# حفظ المفتاح الخاص في ملف keys/private_key.pem
with open("keys/private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()  # لاحقًا بنضيف كلمة مرور
        )
    )

# حفظ المفتاح العام في ملف keys/public_key.pem
with open("keys/public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
# طباعة المفاتيح
# print(public_key.decode())
# print(private_key.decode())