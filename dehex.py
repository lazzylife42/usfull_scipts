import base64

def complex_decrypt(encrypted, key):
    decrypted = bytearray()
    key_length = len(key)
    for i, char in enumerate(encrypted):
        key_char = ord(key[i % key_length])
        decrypted_char = (char ^ key_char - i - key_char) % 256
        decrypted.append(decrypted_char)
    return decrypted

def decrypt_hex(encrypted_hex, key):
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    return complex_decrypt(encrypted_bytes, key)

def decrypt_base64(encrypted_base64, key):
    encrypted_bytes = base64.b16decode(encrypted_base64, casefold=True)
    return complex_decrypt(encrypted_bytes, key)

if __name__ == "__main__":
    encrypted_hex = "aa9da3b6d8db819fc89add88c08f9792c1848f81c4799596cf9c7f7dd17e"
    key = "examplekey"

    decrypted_hex = decrypt_hex(encrypted_hex, key)
    print(f"Decrypted Message (hex): {decrypted_hex.hex()}")

    try:
        decrypted_base64 = decrypt_base64(encrypted_hex.upper(), key)
        print(f"Decrypted Message (Base64): {decrypted_base64.decode('utf-8')}")
    except Exception as e:
        print("Unable to decode as Base64:", e)

