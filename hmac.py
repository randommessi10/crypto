import hmac
import hashlib

# secret key
key = b'secret_key'

# message
message = b'Hello World'

# create HMAC
hmac_result = hmac.new(key, message, hashlib.sha256)

# get hexadecimal result
final_hmac = hmac_result.hexdigest()

print("HMAC:", final_hmac)