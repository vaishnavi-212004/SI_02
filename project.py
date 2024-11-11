# Function to encrypt a message using Caesar Cipher
def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is an alphabet
            # Shift character and handle both lowercase and uppercase
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Keep non-alphabet characters unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt a message using Caesar Cipher
def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is an alphabet
            # Shift character back and handle both lowercase and uppercase
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Keep non-alphabet characters unchanged
            decrypted_text += char
    return decrypted_text

# Main program to demonstrate encryption and decryption
def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (key): "))

    encrypted_message = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
