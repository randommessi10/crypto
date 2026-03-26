alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plaintext,shift):
    ciphertext = ''
    for i in plaintext:
        new_index = (alphabets.index(i)+shift)%26
        newchar = alphabets[new_index]
        ciphertext += newchar
    return ciphertext

def decrypt(ciphertext,shift):
    plaintext = ''
    for i in ciphertext:
        new_index = (alphabets.index(i)-shift)%26
        newchar = alphabets[new_index]
        plaintext += newchar
    return plaintext

text = input("Enter your text: ")
shift = int(input("Enter shift: "))
ciphertext = encrypt(text, shift)
print(f"Encrypted text: {ciphertext}")
print(f"Decrypted text: {decrypt(ciphertext, shift)}")
    
