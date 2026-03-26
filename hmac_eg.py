import hmac
import hashlib

# secret key
key = 'secret_key'.encode()

# message
message = 'Hello World'.encode()

# create HMAC
hmac_result = hmac.new(key, message, hashlib.sha256)

# get hexadecimal result
final_hmac = hmac_result.hexdigest()

print("HMAC:", final_hmac)