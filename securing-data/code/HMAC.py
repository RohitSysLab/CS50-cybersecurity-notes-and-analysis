import hmac
import hashlib

# key and message must be bytes because cryptographic algorithms requires raw bytes
key = b"key"  # b is a syntax in python that declares it to be bytes

message = input("please type here something: ").encode()  #.encode() is a function that converts it to bytes

# sender generates HMAC
h = hmac.new(key, message, hashlib.sha256)
digest = h.hexdigest()

print("Generated HMAC:", digest)

# --- verification simulation ---

received_message = message
received_digest = digest

# receiver recomputes HMAC
new_hmac = hmac.new(key, received_message, hashlib.sha256).hexdigest()

# comparison between sender message and received messaged
if hmac.compare_digest(received_digest, new_hmac): #the hmac.compare_digest function prevents attacks like timing analysis by hacker,it takes same amount of time for all different number of value
    print("Verification successful: message is authentic")
else:
    print("Verification failed: message was modified")
