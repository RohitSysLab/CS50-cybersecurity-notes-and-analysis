import os, hashlib

def plain_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def salted_hash(text):
    salt = os.urandom(16)                     # random 128‑bit salt
    salted = salt + text.encode()             # prepend salt
    return salt.hex(), hashlib.sha256(salted).hexdigest()

# demo
s = input("type something: ")
plain = plain_hash(s)
salt_hex, salted = salted_hash(s)

print("plain hash :", plain)
print("salt (hex) :", salt_hex)
print("salted hash:", salted)
