def encrypt(text, key):
    while (len(text) % len(key) != 0):
        text += 'x'

    columns = {}
    for letter in key:
        columns[letter] = ''

    position = 0
    for character in text:
        key_char = key[position % len(key)]
        columns[key_char] = columns[key_char] + character
        position += 1

    cipher = ''
    for letter in sorted(key):
        cipher = cipher + columns[letter]

    return cipher


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