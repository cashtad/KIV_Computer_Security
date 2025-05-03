import hashlib

def hash_text(text: str) -> bytes:
    return hashlib.sha256(text.encode("utf-8")).digest()
