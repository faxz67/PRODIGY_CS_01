def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Use 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g. 3): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    if choice == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted Message: {result}")
    else:
        result = decrypt(message, shift)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
