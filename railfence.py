def encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    
    row = 0
    direction = 1 

    for char in plaintext:
        fence[row].append(char)
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    result = ""
    #To check : print(fence)
    for char in fence:
        result += "".join(char)

    return result


text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
cipher = encrypt(text, rails)
print("Ciphertext:", cipher)