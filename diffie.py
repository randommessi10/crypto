p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter private key of User1: "))
b = int(input("Enter private key of User2: "))

A = (g**a) % p
B = (g**b) % p

print("Public key of User1:", A)
print("Public key of User2:", B)

key1 = (B**a) % p
key2 = (A**b) % p

print("Shared key for User1:", key1)
print("Shared key for User2:", key2)