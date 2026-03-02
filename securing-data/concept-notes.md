
# Securing Data – CS50 Cybersecurity


### Hash Functions
we can think Hash functions as mathematical functions or algorithms that helps in protecting data by converting input data into hash value.Below are discussed two types of Hashing functions (both cryptographic and non cryptographic)

# SHA Family:
SHA-1, 
SHA-2: SHA-224, SHA-256, SHA-384, SHA-512 (widely used, secure).
SHA-3 
# others
RIPEMD: RIPEMD-128, RIPEMD-160 (used in blockchain).
Whirlpool,
MD Series: MD2, MD4, MD5 (now outdated because of vulnerabilities)

# Below ones are Used for message authentication,
HMAC (Hash-based Message Authentication Code). 
KMAC (based on Keccak). 
Poly1305-AES, SipHash, VMAC, UMAC: Fast, used in network protocols and authentication.
(check "HMAC.py" where I have shown some basic demonstration)


### Hashing 
hashing refers to the process of implementation of hash function on input data
(check hashing.py where I demonstrated it conceptually)


### Salting
salting generally means adding a random value to a input data before its hashed, making it really hard for the attacker to crack it by costing time,energy and money 
(check salting.py where I demonstrated it conceptually)





