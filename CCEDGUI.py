import tkinter as tk
from tkinter import messagebox

def caesar_shift(text, shift, encode=True):
    shifted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shift = shift if encode else -shift
            shifted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def on_encode():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encoded_text = caesar_shift(text, shift, encode=True)
    result_label.config(text=f"Encoded Text: {encoded_text}")
    result_text.set(encoded_text)
    messagebox.showinfo("Caesar Cipher", f"Encoded Text: {encoded_text}")

def on_decode():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    decoded_text = caesar_shift(text, shift, encode=False)
    result_label.config(text=f"Decoded Text: {decoded_text}")
    result_text.set(decoded_text)
    messagebox.showinfo("Caesar Cipher", f"Decoded Text: {decoded_text}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())
    messagebox.showinfo("Caesar Cipher", "Text copied to clipboard!")

def save_encoded():
    encoded_text = result_text.get()
    with open("encoded_text.txt", "w") as file:
        file.write(encoded_text)
    messagebox.showinfo("Caesar Cipher", "Encoded text saved to 'encoded_text.txt'!")

def load_encoded():
    try:
        with open("encoded_text.txt", "r") as file:
            encoded_text = file.read()
        result_text.set(encoded_text)
        messagebox.showinfo("Caesar Cipher", "Encoded text loaded from 'encoded_text.txt'!")
    except FileNotFoundError:
        messagebox.showwarning("Caesar Cipher", "No encoded text found!")

def clear_encoded():
    try:
        open("encoded_text.txt", "w").close()
        result_text.set("")
        messagebox.showinfo("Caesar Cipher", "Encoded text file cleared!")
    except FileNotFoundError:
        messagebox.showwarning("Caesar Cipher", "No encoded text found!")

def save_decoded():
    decoded_text = result_text.get()
    with open("decoded_text.txt", "w") as file:
        file.write(decoded_text)
    messagebox.showinfo("Caesar Cipher", "Decoded text saved to 'decoded_text.txt'!")

def load_decoded():
    try:
        with open("decoded_text.txt", "r") as file:
            decoded_text = file.read()
        result_text.set(decoded_text)
        messagebox.showinfo("Caesar Cipher", "Decoded text loaded from 'decoded_text.txt'!")
    except FileNotFoundError:
        messagebox.showwarning("Caesar Cipher", "No decoded text found!")

def clear_decoded():
    try:
        open("decoded_text.txt", "w").close()
        result_text.set("")
        messagebox.showinfo("Caesar Cipher", "Decoded text file cleared!")
    except FileNotFoundError:
        messagebox.showwarning("Caesar Cipher", "No decoded text found!")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")

# Create and place the components
tk.Label(root, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Shift (0-25):").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

encode_button = tk.Button(root, text="Encode", command=on_encode)
encode_button.grid(row=2, column=0, padx=10, pady=10)

decode_button = tk.Button(root, text="Decode", command=on_decode)
decode_button.grid(row=2, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", font=('Helvetica', 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_text = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_text, state='readonly', width=40)
result_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, padx=10, pady=10)

save_encoded_button = tk.Button(root, text="Save Encoded", command=save_encoded)
save_encoded_button.grid(row=5, column=1, padx=10, pady=10)

load_encoded_button = tk.Button(root, text="Load Encoded", command=load_encoded)
load_encoded_button.grid(row=6, column=0, padx=10, pady=10)

clear_encoded_button = tk.Button(root, text="Clear Encoded", command=clear_encoded)
clear_encoded_button.grid(row=6, column=1, padx=10, pady=10)

save_decoded_button = tk.Button(root, text="Save Decoded", command=save_decoded)
save_decoded_button.grid(row=7, column=0, padx=10, pady=10)

load_decoded_button = tk.Button(root, text="Load Decoded", command=load_decoded)
load_decoded_button.grid(row=7, column=1, padx=10, pady=10)

clear_decoded_button = tk.Button(root, text="Clear Decoded", command=clear_decoded)
clear_decoded_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
