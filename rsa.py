import random
from math import gcd

# Step 1: Choose primes
p = 61
q = 53

# Step 2: Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = random.randrange(2, phi)
while gcd(e, phi) != 1:
    e = random.randrange(2, phi)

# Step 4: Compute d (mod inverse of e)
d = None
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

# Keys
public_key = (e, n)
private_key = (d, n)

print("Public key:", public_key)
print("Private key:", private_key)

# Step 5: Message (number only)
message = 42

# Step 6: Encrypt
cipher = pow(message, e, n)
print("Encrypted:", cipher)

# Step 7: Decrypt
decrypted = pow(cipher, d, n)
print("Decrypted:", decrypted)