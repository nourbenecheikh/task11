def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Shift must be between 0 and 25.")
        except ValueError:
            print("Please enter a valid integer.")

    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed): {result}")

if __name__ == "__main__":
    main()
