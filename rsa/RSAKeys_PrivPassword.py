from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

# genetate keys folder
os.makedirs("keys", exist_ok=True)

# generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# generate public key
public_key = private_key.public_key()

# password for private key
password = b"PrivkeyPassword"  # you could change it

#  save private key using BestAvailableEncryption
with open("keys/private_key_secure.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password)
        )
    )

# saving public key without password
with open("keys/public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )