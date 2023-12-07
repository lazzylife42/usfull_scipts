import sys

def complex_encrypt(message, key):
    encrypted = bytearray()
    key_length = len(key)
    for i, char in enumerate(message):
        key_char = ord(key[i % key_length])
        msg_char = ord(char)
        encrypted_char = (msg_char + key_char + i) % 256
        encrypted.append(encrypted_char ^ key_char)
    return encrypted

if len(sys.argv) != 3:
    print("Usage: python encrypt.py <message> <key>")
else:
    message = sys.argv[1]
    key = sys.argv[2]
    if len(key) < 5:
        print("Error: Key must be at least 5 characters long.")
    else:
        encrypted_message = complex_encrypt(message, key)
        with open('encrypted_message.bin', 'wb') as file:
            file.write(encrypted_message)
        print(f"Encrypted Message saved to encrypted_message.bin")
