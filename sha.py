import hashlib

# take input from user
message = input("Enter message: ")

# convert to bytes
message_bytes = message.encode()

# create SHA-512 hash
hash_object = hashlib.sha512(message_bytes)

# get hex output
hash_result = hash_object.hexdigest()

print("SHA-512 Hash:", hash_result)