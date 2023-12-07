import sys

def complex_decrypt(encrypted, key):
    decrypted = bytearray()
    key_length = len(key)
    for i, char in enumerate(encrypted):
        key_char = ord(key[i % key_length])
        decrypted_char = (char ^ key_char - i - key_char) % 256
        decrypted.append(decrypted_char)
    return decrypted

if len(sys.argv) != 3:
    print("Usage: python decrypt.py <encrypted_file> <key>")
else:
    encrypted_file = sys.argv[1]
    key = sys.argv[2]
    with open(encrypted_file, 'rb') as file:
        encrypted_message = file.read()
        if len(key) < 5:
            print("Error: Key must be at least 5 characters long.")
        else:
            decrypted_message = complex_decrypt(encrypted_message, key)
            print(f"Decrypted Message (hex): {decrypted_message.hex()}")

