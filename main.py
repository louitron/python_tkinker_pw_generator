import tkinter as tk
import random
import string
import pyperclip
## function to generate med/strong passwords
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def generate_easy_password(length):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def generate_button_clicked():
    if strength.get() == "strong":
        password = generate_password(20)
    elif strength.get() == "medium":
        password = generate_password(12)
    elif strength.get() == "easy":
        password = generate_easy_password(8)

    password_output.config(text=password)
    pyperclip.copy(password)

app = tk.Tk()
app.title("Password Generator")

strength = tk.StringVar()

frame = tk.Frame(app)
frame.pack()

strong_radio = tk.Radiobutton(frame, text="Strong", variable=strength, value="strong")
strong_radio.pack(side="left")

medium_radio = tk.Radiobutton(frame, text="Medium", variable=strength, value="medium")
medium_radio.pack(side="left")

easy_radio = tk.Radiobutton(frame, text="Easy", variable=strength, value="easy")
easy_radio.pack(side="left")

generate_button = tk.Button(frame, text="Generate", command=generate_button_clicked)
generate_button.pack(side="left")

password_output = tk.Label(app, text="")
password_output.pack()

app.mainloop()
