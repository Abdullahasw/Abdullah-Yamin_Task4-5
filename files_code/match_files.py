import hashlib

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# الملفات الأصلية
original_files = {
    "fake_data": "test_data/fake_data.json",
    "fake_message": "test_data/fake_message.txt"
}

# الملفات المفكوكة
decrypted_files = {
    "fake_data": "decrypted/fake_data.txt",
    "fake_message": "decrypted/fake_message.txt"
}

# المقارنة
for key in original_files:
    original_hash = hash_file(original_files[key])
    decrypted_hash = hash_file(decrypted_files[key])

    if original_hash == decrypted_hash:
        print(f"✅ {key}: match")
    else:
        print(f"❌ {key}: NOT match")