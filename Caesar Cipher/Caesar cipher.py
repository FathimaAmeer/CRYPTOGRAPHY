def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Take input from user
plaintext = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (key): "))

# Perform encryption
cipher_text = caesar_encrypt(plaintext, shift)

# Perform decryption
decrypted_text = caesar_decrypt(cipher_text, shift)

# Write to a file
with open("caesar_output.txt", "w") as file:
    file.write(f"Original Text: {plaintext}\n")
    file.write(f"Encrypted Text: {cipher_text}\n")
    file.write(f"Decrypted Text: {decrypted_text}\n")

print("Encryption and decryption complete. Output saved to 'caesar_output.txt'.")
