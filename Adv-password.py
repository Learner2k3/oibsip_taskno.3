import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please choose at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_clicked():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value for password length.")
        return

    if length <= 0:
        messagebox.showerror("Error", "Password length must be a positive value.")
        return

    use_letters = letters_var.get() == 1
    use_numbers = numbers_var.get() == 1
    use_symbols = symbols_var.get() == 1

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        result_label.config(text=f"Generated Password: {password}")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.IntVar()
letters_checkbox = tk.Checkbutton(root, text="Include letters", variable=letters_var)
letters_checkbox.pack()

numbers_var = tk.IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=on_generate_clicked)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
