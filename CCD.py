import string
from collections import Counter

def caesar_shift(text, shift):
    shifted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shifted_text.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def get_english_score(text):
    # Frequency of letters in the English language
    english_freq = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92,
        'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
        'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
    }
    text = text.upper()
    text_counter = Counter(filter(str.isalpha, text))
    total_chars = sum(text_counter.values())
    if total_chars == 0:
        return 0
    score = sum((english_freq[char] * (count / total_chars) for char, count in text_counter.items()))
    return score

def caesar_decode(ciphertext):
    potential_plaintexts = [(caesar_shift(ciphertext, shift), shift) for shift in range(26)]
    scored_plaintexts = [(text, shift, get_english_score(text)) for text, shift in potential_plaintexts]
    best_text, best_shift, best_score = max(scored_plaintexts, key=lambda item: item[2])
    return best_text, best_shift

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    plaintext, shift = caesar_decode(ciphertext)
    print(f"Decoded text: {plaintext}")
    print(f"Shift used: {shift}")
