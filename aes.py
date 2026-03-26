from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b'1234567890123456'

text = input("Enter text: ").encode()

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(text,16))

cipher_b64 = base64.b64encode(ciphertext).decode()
print("Ciphertext: ", cipher_b64)

cipher = AES.new(key, AES.MODE_ECB)
decoded = base64.b64decode(cipher_b64)

plaintext = unpad(cipher.decrypt(decoded),16)
print("Decrypted:", plaintext.decode())