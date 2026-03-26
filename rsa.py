from math import gcd

# Step 1: Choose primes
p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))

# Step 2: Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = 2
while gcd(e, phi) != 1:
    e += 1

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
message = int(input("Enter message: "))

# Step 6: Encrypt
cipher = message ** e % n
print("Encrypted:", cipher)

# Step 7: Decrypt
decrypted = cipher ** d % n
print("Decrypted:", decrypted)