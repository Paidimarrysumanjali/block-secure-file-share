import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from secure_share.main import generate_key, encrypt_data, decrypt_data

def test_encryption_decryption():
    key = generate_key()
    data = b"this is a secret message"
    encrypted = encrypt_data(data, key)
    decrypted = decrypt_data(encrypted, key)
    assert decrypted == data
