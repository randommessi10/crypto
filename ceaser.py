alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plaintext):
    ciphertext = ''
    for i in plaintext:
        newchar = alphabets[(alphabets.index(i)+3)%26]
        ciphertext += newchar
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    for i in ciphertext:
        newchar = alphabets[(alphabets.index(i)-3)%26]
        plaintext += newchar
    return plaintext

text = input("Enter your text: ")
ciphertext = encrypt(text)
print(f"Encrypted text: {ciphertext}")
print(f"Decrypted text: {decrypt(ciphertext)}")
    
