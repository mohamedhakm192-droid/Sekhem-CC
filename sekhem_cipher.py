# SEKHEM-CC: Advanced Encryption Engine
import base64

def triad_encrypt(plain_text, key):
    # دمج النص مع المفتاح السري (قانون التثليث)
    combined = f"{plain_text}::{key}"
    encoded = base64.b64encode(combined.encode("utf-8"))
    return encoded.decode("utf-8")

# المفتاح السري
MY_KEY = "SK-TR-2026-X99"

# تجربة حماية رسالة
secret_msg = "الهدف مؤمن تماما"
print(f"🛡️ الشفرة الناتجة: {triad_encrypt(secret_msg, MY_KEY)}")
