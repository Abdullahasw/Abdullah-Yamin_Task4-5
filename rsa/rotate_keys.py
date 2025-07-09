import os
import shutil
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# إعداد التاريخ كمُعرّف (Key ID)
key_id = datetime.today().strftime("%Y%m%d")
archive_dir = f"keys/archive/{key_id}"
os.makedirs(archive_dir, exist_ok=True)

# أرشفة المفاتيح القديمة (إن وُجدت)
if os.path.exists("keys/private_key_secure.pem"):
    shutil.move("keys/private_key_secure.pem", f"{archive_dir}/private_key_secure.pem")

if os.path.exists("keys/public_key.pem"):
    shutil.move("keys/public_key.pem", f"{archive_dir}/public_key.pem")

# توليد مفتاح جديد
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# كلمة مرور جديدة لحماية المفتاح
password = b"anotherprivkeypass"

# حفظ المفتاح الخاص
with open("keys/private_key_secure.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    ))

# حفظ المفتاح العام
with open("keys/public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))