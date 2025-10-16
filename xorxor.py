import itertools

# Given values
k1 = bytes.fromhex("3c3f0193af37d2ebbc50cc6b91d27cf61197")
k21 = bytes.fromhex("ff76edcad455b6881b92f726987cbf30c68c")
k23 = bytes.fromhex("611568312c102d4d921f26199d39fe973118")
k1234 = bytes.fromhex("91ec5a6fa8a12f908f161850c591459c3887")
f45 = bytes.fromhex("0269dd12fe3435ea63f63aef17f8362cdba8")

bxor = lambda a,b: bytes(x ^ y for x, y in zip(a, b))


k4 = bxor(bxor(k1234, k23), k1)

f5 = bxor(f45, k4)

ff = b'cry{'

k5 = bxor(ff, f5[:4])

k5 = (k5 * (len(f5) // 4 + 1))[:len(f5)]

# Decrypt the flag
flag = bxor(f5, k5)
print(flag.decode())