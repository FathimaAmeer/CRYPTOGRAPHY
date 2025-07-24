def generate_key(text, key):
    key = key.upper()
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = generate_key(plaintext, key)
    cipher_text = ""

    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = (ord(p) + ord(k)) % 26
            cipher_text += chr(shift + ord('A'))
        else:
            cipher_text += p
    return cipher_text

def decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    orig_text = ""

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = (ord(c) - ord(k) + 26) % 26
            orig_text += chr(shift + ord('A'))
        else:
            orig_text += c
    return orig_text

# --- Main Program ---
plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")

ciphertext = encrypt(plaintext, keyword)
decrypted = decrypt(ciphertext, keyword)

# Show on screen
print(f"Encrypted Text: {ciphertext}")
print(f"Decrypted Text: {decrypted}")

# Save to file
with open("vigenere_output.txt", "w") as file:
    file.write(f"Keyword: {keyword}\n")
    file.write(f"Plaintext: {plaintext}\n")
    file.write(f"Encrypted: {ciphertext}\n")
    file.write(f"Decrypted: {decrypted}\n")
