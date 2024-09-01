def caesar_shift(text, shift):
    shifted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shifted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def caesar_encode(plaintext, shift):
    return caesar_shift(plaintext, shift)

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift (0-25): "))
    ciphertext = caesar_encode(plaintext, shift)
    print(f"Encoded text: {ciphertext}")
