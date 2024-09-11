# Password Generator By Cedric Arts

# Importing necessary modules/libraries
import random
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Window
app = tk.Tk()
app.geometry('500x500')
app.title("Password Generator By CA")

# Boolean Variables for options
char_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
sym_var = tk.BooleanVar()

password = ""

# File to store the passwords
password_file = 'passwords.json'

# Function to save passwords to file
def SavePassword(password):
    if not os.path.exists(password_file):
        with open(password_file, 'w') as file:
            json.dump([], file)
    
    with open(password_file, 'r+') as file:
        data = json.load(file)
        data.append(password)
        file.seek(0)
        json.dump(data, file)
    
    # Update listbox with new password
    password_listbox.insert(tk.END, password)

# Function to load passwords when app starts
def LoadPasswords():
    if os.path.exists(password_file):
        with open(password_file, 'r') as file:
            data = json.load(file)
            for pwd in data:
                password_listbox.insert(tk.END, pwd)

# Function to generate a password
def GeneratePassword():
    pass1 = []

    if char_var.get():
        pass1.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                      'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'H',
                      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                      'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    if digits_var.get():
        pass1.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    if sym_var.get():
        pass1.extend(['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', 
                      ']', '[', '\'', ';', '"', '?', '>', '<', '~', '`',
                      '.', ',', '=', '_', '-', '+', '(', ')', '|'])

    global password
    password = ""

    for x in range(entry_length.get()):
        password += random.choice(pass1)

    result_label.config(text=f"Your new password is:\n {password}")
    SavePassword(password)

# Function to copy password to clipboard
def CopyPassword():
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        result_label.config(text="Password copied to clipboard!")

# Input Widgets
input_frame = ttk.Frame(master=app, padding=10)
input_frame.pack(fill='x')

# Length input and checkboxes
entry_label = ttk.Label(master=input_frame, text='Enter length of password:', font='Arial 14')
entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_length = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_length)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

chkChar = ttk.Checkbutton(master=input_frame, text="Characters", variable=char_var)
chkChar.grid(row=1, column=0, padx=5, pady=5, sticky="w")
chkNumber = ttk.Checkbutton(master=input_frame, text="Digits", variable=digits_var)
chkNumber.grid(row=1, column=1, padx=5, pady=5, sticky="w")
chkSym = ttk.Checkbutton(master=input_frame, text="Symbols", variable=sym_var)
chkSym.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Generate and copy buttons
button = ttk.Button(master=input_frame, text='Generate', command=GeneratePassword)
button.grid(row=2, column=0, padx=5, pady=10, sticky="w")
button_copy = ttk.Button(master=input_frame, text='Copy Password', command=CopyPassword)
button_copy.grid(row=2, column=1, padx=5, pady=10, sticky="w")

# Display area for the most recent password
result_label = ttk.Label(master=app, text="", font='Arial 12', padding=10)
result_label.pack(fill='x', pady=5)

# Password history section with scrollable listbox
history_frame = ttk.Frame(master=app, padding=10)
history_frame.pack(fill='both', expand=True)

history_label = ttk.Label(master=history_frame, text="Saved Passwords:", font='Arial 14')
history_label.pack(anchor='w')

password_listbox = tk.Listbox(history_frame, height=8)
password_listbox.pack(side='left', fill='both', expand=True, padx=5)

# Scrollbar for password listbox
scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=password_listbox.yview)
password_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Load saved passwords on start
LoadPasswords()

# Run Application
app.mainloop()
