import cv2
import numpy as np

def load_image(path):
    return cv2.imread(path)

def save_image(path, image):
    cv2.imwrite(path, image)

def encrypt_image(image, key):
    print("Encrypting image...")
    rows, cols, _ = image.shape
    encrypted = np.copy(image)

    for i in range(rows):
        for j in range(cols):
            # Conversion en int pour éviter l'overflow, traitement sur chaque canal (R, G, B)
            encrypted[i, j] = (image[rows - i - 1, cols - j - 1].astype(int) + key) % 256
    return encrypted

def decrypt_image(image, key):
    print("Decrypting image...")
    rows, cols, _ = image.shape
    decrypted = np.copy(image)

    for i in range(rows):
        for j in range(cols):
            orig_i = rows - i - 1
            orig_j = cols - j - 1
            # Conversion en int pour éviter l'overflow, traitement sur chaque canal (R, G, B)
            decrypted[orig_i, orig_j] = (image[i, j].astype(int) - key) % 256
    return decrypted

def main():
    print("=== Image Encryption Tool ===")
    path = input("Enter the image path: ")
    key = int(input("Enter the encryption key (integer): "))

    image = load_image(path)
    if image is None:
        print("Error: Image not found. Please check the path.")
        return

    mode = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()

    if mode == 'E':
        encrypted = encrypt_image(image, key)
        save_image('encrypted_image.png', encrypted)
        print("Image encrypted and saved as 'encrypted_image.png'")
    elif mode == 'D':
        decrypted = decrypt_image(image, key)
        save_image('decrypted_image.png', decrypted)
        print("Image decrypted and saved as 'decrypted_image.png'")
    else:
        print("Invalid option. Please type 'E' or 'D'.")

if __name__ == "__main__":
    main()
