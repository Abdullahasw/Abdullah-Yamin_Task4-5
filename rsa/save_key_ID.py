from datetime import datetime

key_id = datetime.now().strftime("%Y%m%d")

with open("encrypted/fake_data.meta", "w") as meta:
    meta.write(f"Key-ID: {key_id}")