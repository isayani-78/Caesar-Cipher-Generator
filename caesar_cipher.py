import string

chars = string.ascii_letters + string.digits + string.punctuation

def caesar(text, shift):
    return ''.join(chars[(chars.index(c) + shift) % 26] if c in chars else c for c in text)

msg = input("Enter message: ")
key = int(input("Enter key: "))

enc = caesar(msg, key)
dec = caesar(enc, -key)

print("Encrypted:", enc)
print("Decrypted:", dec)
