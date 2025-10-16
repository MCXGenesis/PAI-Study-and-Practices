from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

p = getPrime(1024) # rsa
q = getPrime(1024) # rsa
p_dh = getPrime(2048) # dh pow
g = getPrime(512) # dh base
a = getPrime(512) # dh alice
b = getPrime(512) # dh bob

def generate_public_int(g, a, p):
    return g ^ a % p #should be pow, vuln

def generate_shared_secret(A, b, p):
    return A ^ b % p # should be pow, vuln

n = p * q # rsa
e = 3 # rsa, public key pair (e,n)
flag = b'kuro'
flag_int = bytes_to_long(flag)
A = generate_public_int(g,a,p_dh) # dh
B = generate_public_int(g,b,p_dh) # dh
shared_int = generate_shared_secret(A, b, p_dh) # dh, but mod too smol
flag2 = flag_int ^ shared_int 
c = pow(flag2, e, n) # rsa, ciphertext

# # ---
# t = (p-1)*(q-1)
# # e smaller than t && e coprime with t
# d = gmpy2.invert(e, t)
# # d multiplicative inverse of  e mod t



print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")
print(f"p_dh = {p_dh}")
print(f"g = {g}")
print(f"A = {A}")
print(f"B = {B}")
print(f"t = {t}")

# bxor = lambda a,b: bytes(x ^ y for x, y in zip(a, b))

# b = B^g
# shared_int = A^b
# flag2 ,_ = gmpy2.iroot(c,e)
# flag = flag2^shared_int
# flag = long_to_bytes(flag)

# print(flag.decode())