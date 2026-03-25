alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plaintext, key):
    ciphertext = ""
    if len(plaintext) != len(key):
        return "Key and plaintext must have the same length"
    for i in range(len(plaintext)):
        p_index = alphabets.index(plaintext[i])
        k_index = alphabets.index(key[i])
        c_index = (p_index + k_index) % 26
        ciphertext += alphabets[c_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    if len(ciphertext) != len(key):
        return "Key and ciphertext must have the same length"
    for i in range(len(ciphertext)):
        c_index = alphabets.index(ciphertext[i])
        k_index = alphabets.index(key[i])
        p_index = (c_index - k_index) % 26
        plaintext += alphabets[p_index]
    return plaintext

text = input("Enter plaintext: ")
key = input("Enter key: ")

cipher = encrypt(text, key)
print("Ciphertext:", cipher)

plain = decrypt(cipher, key)
print("Decrypted text:", plain)