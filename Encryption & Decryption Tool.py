print("------------------------------------------------------------------------------------------Encryption & Decryption Tool---------------------------------------------------------------")
import random
import os as os
file_path = "encrypted_text.txt"
def encrypt(text):
    x = text.strip()
    encrypted_text = ""
    for i in range(len(x)):
        encrypted_text += str(random.randint(0, len(x)) + i + random.randint(0, len(x)))
    return encrypted_text
def decrypt(encrypted_text):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += str(random.randint(0, len(encrypted_text)) + i + random.randint(0, len(encrypted_text)))
    return decrypted_text
def main():
    while True:
        print("\n--- Encryption & Decryption Tool ---")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            text = input("Enter the text you want to encrypt: ")
            encrypted_text = encrypt(text)
            print("Encrypted text:", encrypted_text)
            with open(file_path, "w") as f:
                f.write(encrypted_text)
        elif choice == "2":
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    encrypted_text = f.read()
                decrypted_text = decrypt(encrypted_text)
                print("Decrypted text:", decrypted_text)
            else:
                print("No encrypted text found.")
        elif choice == "5":
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
print("Decrypted text:", decrypted_text)