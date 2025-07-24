import numpy as np
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26")

    # Adjugate matrix
    adjugate = np.array([[matrix[1][1], -matrix[0][1]],
                         [-matrix[1][0], matrix[0][0]]])
    inv_matrix = (det_inv * adjugate) % modulus
    return inv_matrix.astype(int)

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num % 26 + ord('A')) for num in numbers])

def prepare_text(text, block_size):
    text = text.upper().replace(" ", "").replace("J", "I")
    while len(text) % block_size != 0:
        text += 'X'
    return text

def encrypt(plaintext, key_matrix):
    block_size = len(key_matrix)
    plaintext = prepare_text(plaintext, block_size)
    encrypted = []

    for i in range(0, len(plaintext), block_size):
        block = text_to_numbers(plaintext[i:i+block_size])
        vector = np.array(block).reshape((block_size, 1))
        result = np.dot(key_matrix, vector) % 26
        encrypted.extend(result.flatten())

    return numbers_to_text(encrypted)

def decrypt(ciphertext, key_matrix):
    block_size = len(key_matrix)
    decrypted = []

    try:
        inv_matrix = matrix_mod_inv(key_matrix, 26)
    except ValueError as e:
        return str(e)

    for i in range(0, len(ciphertext), block_size):
        block = text_to_numbers(ciphertext[i:i+block_size])
        vector = np.array(block).reshape((block_size, 1))
        result = np.dot(inv_matrix, vector) % 26
        decrypted.extend(result.flatten())

    return numbers_to_text(decrypted)

# --- Main Program ---
# 2x2 Key Matrix
print("Enter the 2x2 key matrix (4 integers, row-wise):")
key = list(map(int, input("e.g., 3 3 2 5: ").split()))
key_matrix = np.array(key).reshape((2, 2))

plaintext = input("Enter plaintext: ").upper()

ciphertext = encrypt(plaintext, key_matrix)
decrypted = decrypt(ciphertext, key_matrix)

# Save to file
with open("hill_output.txt", "w") as f:
    f.write(f"Key Matrix:\n{key_matrix}\n")
    f.write(f"Plaintext: {plaintext}\n")
    f.write(f"Encrypted: {ciphertext}\n")
    f.write(f"Decrypted: {decrypted}\n")

# Show output
print(f"Encrypted Text: {ciphertext}")
print(f"Decrypted Text: {decrypted}")
print("Output saved to 'hill_output.txt'")
