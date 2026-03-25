alphabets = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = input("Enter your key: ")
key = key.replace("j","i")

matrixOrder = []
for letter in key:
    if letter not in matrixOrder:
        matrixOrder.append(letter)
for letter in alphabets:
    if letter not in matrixOrder:
        matrixOrder.append(letter)

matrix = []
index = 0
for i in range(5):
    row = []
    for j in range(5):
        row.append(matrixOrder[index])
        index+=1
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)

def find_position(char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i,j

def encrypt(plaintext):
    plaintext = plaintext.replace("j","i")
    ciphertext = ""
    splitpairs = []
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]

        if i+1 < len(plaintext):
            char2 = plaintext[i+1]
            if char1 == char2:
                splitpairs.append(char1 + 'x')
                i += 1
            else:
                splitpairs.append(char1 + char2)
                i += 2
        else:
            splitpairs.append(char1 + 'x')
            i += 1

    print("Pairs:", splitpairs)
    for pair in splitpairs:
        char1 = pair[0]
        char2 = pair[1]
        row1,col1 = find_position(char1)
        row2,col2 = find_position(char2)
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5]
            ciphertext += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1]
            ciphertext += matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    splitpairs = []
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        splitpairs.append(char1 + char2)
        i += 2
    for pair in splitpairs:
        char1 = pair[0]
        char2 = pair[1]
        row1,col1 = find_position(char1)
        row2,col2 = find_position(char2)
        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5]
            plaintext += matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1]
            plaintext += matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext
    
text = input("Enter your text: ")
print("Ciphertext:", encrypt(text))
print("Plaintext:", decrypt(encrypt(text)))