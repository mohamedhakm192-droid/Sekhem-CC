import hashlib
import base64

def triad_encrypt(text, key):
    # 1. generate hash from key
    key_hash = hashlib.sha256(key.encode()).hexdigest()
    
    # 2. combine بطريقة أفضل
    combined = f"{text}|{key_hash[:16]}"
    
    # 3. encode
    return base64.b64encode(combined.encode()).decode()


def triad_decrypt(cipher, key):
    try:
        decoded = base64.b64decode(cipher).decode()
        text, received_hash = decoded.split("|")
        
        expected_hash = hashlib.sha256(key.encode()).hexdigest()[:16]
        
        if received_hash == expected_hash:
            return text
        else:
            return "❌ Invalid key"
    except:
        return "⚠️ Corrupted data"
