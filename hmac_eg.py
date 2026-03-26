import hmac
import hashlib

# secret key
key = 'secret_key'.encode()

# message
message = 'Hello World'.encode()

# create HMAC
hmac_object = hmac.new(key, message, hashlib.sha256)

# get hexadecimal result
hmac_result = hmac_object.hexdigest()

print("HMAC:", hmac_result)