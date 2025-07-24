import re

def generate_key_square(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    key_square = []

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_square.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            key_square.append(char)

    return [key_square[i:i+5] for i in range(0, 25, 5)]

def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace('J', 'I'))
    digraphs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    if len(digraphs[-1]) == 1:
        digraphs[-1] += 'X'
    return digraphs

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
    elif col1 == col2:
        return matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
    elif col1 == col2:
        return matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, key):
    matrix = generate_key_square(key)
    digraphs = prepare_text(text)
    return ''.join([encrypt_pair(a, b, matrix) for a, b in digraphs])

def decrypt(ciphertext, key):
    matrix = generate_key_square(key)
    digraphs = prepare_text(ciphertext)
    return ''.join([decrypt_pair(a, b, matrix) for a, b in digraphs])

# --- Main execution ---
# Input from user
key = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")

# Encrypt and Decrypt
cipher = encrypt(plaintext, key)
decrypted = decrypt(cipher, key)

# Save to file
with open("playfair_output.txt", "w") as file:
    file.write(f"Keyword: {key}\n")
    file.write(f"Plaintext: {plaintext}\n")
    file.write(f"Encrypted: {cipher}\n")
    file.write(f"Decrypted: {decrypted}\n")

# Show result
print(f"Encrypted Text: {cipher}")
print(f"Decrypted Text: {decrypted}")
print("Output saved to 'playfair_output.txt'")
