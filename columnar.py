def encrypt(plaintext, key):
    while (len(plaintext) % len(key) != 0):
        plaintext += 'x'

    columns = {}
    for letter in key:
        columns[letter] = ''

    position = 0
    for char in plaintext:
        key_char = key[position % len(key)]
        columns[key_char] += char
        position += 1

    ciphertext = ''
    for letter in sorted(key):
        ciphertext += columns[letter]

    return ciphertext


def decrypt(cipher, key):
    key_length = len(key)
    column_size = len(cipher) // key_length

    columns = {}
    for letter in key:
        columns[letter] = ''

    position = 0
    for letter in sorted(key):
        for count in range(column_size):
            columns[letter] = columns[letter] + cipher[position]
            position += 1

    text = ''
    for row in range(column_size):
        for letter in key:
            text = text + columns[letter][row]

    return text


key = input("Enter key: ")
text = input("Enter text: ")

cipher = encrypt(text, key)
print("Ciphertext:", cipher)

plain = decrypt(cipher, key)
print("Plaintext:", plain)