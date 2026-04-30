
def simple_hash():
    data=input("please enter a number: ")
    """
    Steps:
    1. Convert the input to a sequence of integers (bytes).
    2. Start with a seed value.
    3. For each byte, combine it with the seed (add + multiply).
    4. Return the seed modulo a large prime → fixed length.
    """        
    # 1️⃣  Turn the input into a list of small integers (0‑255)
    #    .encode() works for strings; for bytes you can skip this step.
    if isinstance(data, str):
        data = data.encode('utf-8')          # e.g. "hello" → b'hello'

    # 2️⃣  Seed – can be any number. 0x123456789ABCDEF is just a nice big constant.
    seed = 0x123456789ABCDEF

    # 3️⃣  Mix each byte into the seed.
    for b in data:               # b is an integer 0‑255
        # Combine the byte with the current seed.
        #   * add   – makes the seed change a little bit.
        #   * multiply – spreads the influence of the byte across the whole seed.
        seed = (seed + b) * 31   # 31 is a small prime; any odd number works.

    # 4️⃣  Reduce to a fixed length.
    #    Using a large prime (here 2**64) keeps the result large enough
    #    while still fitting into a normal Python integer.
    prime = 2**64
    return seed % prime
    print(prime)
print(simple_hash())
