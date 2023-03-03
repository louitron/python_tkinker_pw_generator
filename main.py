import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password(length):
    words = [
  "Jogger",
  "Racoon",
  "Pear",
  "Orange",
  "Mirror",
  "Tuxedo",
  "Goblet",
  "Cabbage",
  "Handcuffs",
  "Honeycomb",
  "Skyscraper",
  "Mustache",
  "Dagger",
  "Parachute",
  "Lighthouse",
  "Spade",
  "Butterfly",
  "Harmonica",
  "Whistle",
  "Jacket",
  "Bowtie",
  "Cannon",
  "Accordion",
  "Mushroom",
  "Asparagus",
  "Hose",
  "Gargoyle",
  "Banister",
  "Teapot",
  "Mandolin",
  "Seagull",
  "Mosquito",
  "Harp",
  "Jackhammer",
  "Goose",
  "Gong",
  "Binoculars",
  "Claw",
  "Ruler",
  "Bathtub",
  "Sunglasses",
  "Washer",
  "Saxophone",
  "Wallet",
  "Rollercoaster",
  "Cheeseburger",
  "Popsicle",
  "Trombone",
  "Elevator",
  "Banjo",
  "Carrot",
  "Kangaroo",
  "Hairbrush",
  "Umbrella",
  "Waterfall",
  "Bookshelf",
  "Sombrero",
  "Sushi",
  "Saddle",
  "Xylophone",
  "Blender",
  "Javelin",
  "Leopard",
  "Fingernail",
  "Dolphin",
  "Trampoline",
  "Motorcycle",
  "Snowflake",
  "Spaceship",
  "Broccoli",
  "Pinecone",
  "Seahorse",
  "Penguin",
  "Rhinoceros",
  "Ping-pong",
  "Barbecue",
  "Volcano",
  "Meatball",
  "Electricity",
  "Giraffe",
  "Sunflower",
  "Eraser",
  "Toothbrush",
  "Dandelion",
  "Telephone",
  "Balloon",
  "Magazine",
  "Popsicle",
  "Kettle",
  "Toaster",
  "Peacock",
  "Binoculars",
  "Maracas",
  "Whisk",
  "Rooster",
  "Saw",
  "Barometer",
  "Candle",
  "Teddy-bear",
  "Yo-yo",
  "Corkscrew",
  "Squirrel",
  "Nail",
  "Refrigerator",
  "Stoplight",
  "Wrench",
  "Raccoon",
  "Trumpet",
  "Toucan",
  "Rubber-band",
  "Radio",
  "Caterpillar",
  "Dumbbell",
  "Rattlesnake",
  "Tweezers",
  "Stethoscope",
  "Fire-extinguisher",
  "Lawnmower",
  "Sneaker",
  "Drumstick",
  "Sardine",
  "Toothpaste",
  "Pretzel",
  "Cassette",
  "Key",
  "Suitcase",
  "Airplane",
  "Hotdog",
  "Almond",
  "Keyboard",
  "Gumball",
  "Baseball",
  "Mermaid",
  "Dragonfly",
  "Umbrella",
  "Sewing-machine",
  "Waffle",
  "Butterfly",
  "Lampshade",
  "Yacht",
    ]
    symbols = string.punctuation
    password = ''
    while len(password) < length:
        word = random.choice(words)
        if len(password + word) <= length:
            password += word
        else:
            break
        if len(password) < length:
            password += random.choice(string.digits + symbols)
    password = ''.join(random.sample(password, len(password)))
    return password

def generate_easy_password(length):
    words = [
  "Jogger",
  "Racoon",
  "Pear",
  "Orange",
  "Mirror",
  "Tuxedo",
  "Goblet",
  "Cabbage",
  "Handcuffs",
  "Honeycomb",
  "Skyscraper",
  "Mustache",
  "Dagger",
  "Parachute",
  "Lighthouse",
  "Spade",
  "Butterfly",
  "Harmonica",
  "Whistle",
  "Jacket",
  "Bowtie",
  "Cannon",
  "Accordion",
  "Mushroom",
  "Asparagus",
  "Hose",
  "Gargoyle",
  "Banister",
  "Teapot",
  "Mandolin",
  "Seagull",
  "Mosquito",
  "Harp",
  "Jackhammer",
  "Goose",
  "Gong",
  "Binoculars",
  "Claw",
  "Ruler",
  "Bathtub",
  "Sunglasses",
  "Washer",
  "Saxophone",
  "Wallet",
  "Rollercoaster",
  "Cheeseburger",
  "Popsicle",
  "Trombone",
  "Elevator",
  "Banjo",
  "Carrot",
  "Kangaroo",
  "Hairbrush",
  "Umbrella",
  "Waterfall",
  "Bookshelf",
  "Sombrero",
  "Sushi",
  "Saddle",
  "Xylophone",
  "Blender",
  "Javelin",
  "Leopard",
  "Fingernail",
  "Dolphin",
  "Trampoline",
  "Motorcycle",
  "Snowflake",
  "Spaceship",
  "Broccoli",
  "Pinecone",
  "Seahorse",
  "Penguin",
  "Rhinoceros",
  "Ping-pong",
  "Barbecue",
  "Volcano",
  "Meatball",
  "Electricity",
  "Giraffe",
  "Sunflower",
  "Eraser",
  "Toothbrush",
  "Dandelion",
  "Telephone",
  "Balloon",
  "Magazine",
  "Popsicle",
  "Kettle",
  "Toaster",
  "Peacock",
  "Binoculars",
  "Maracas",
  "Whisk",
  "Rooster",
  "Saw",
  "Barometer",
  "Candle",
  "Teddy-bear",
  "Yo-yo",
  "Corkscrew",
  "Squirrel",
  "Nail",
  "Refrigerator",
  "Stoplight",
  "Wrench",
  "Raccoon",
  "Trumpet",
  "Toucan",
  "Rubber-band",
  "Radio",
  "Caterpillar",
  "Dumbbell",
  "Rattlesnake",
  "Tweezers",
  "Stethoscope",
  "Fire-extinguisher",
  "Lawnmower",
  "Sneaker",
  "Drumstick",
  "Sardine",
  "Toothpaste",
  "Pretzel",
  "Cassette",
  "Key",
  "Suitcase",
  "Airplane",
  "Hotdog",
  "Almond",
  "Keyboard",
  "Gumball",
  "Baseball",
  "Mermaid",
  "Dragonfly",
  "Umbrella",
  "Sewing-machine",
  "Waffle",
  "Butterfly",
  "Lampshade",
  "Yacht",
    ]
    symbols = string.punctuation
    password = ''
    while len(password) < length:
        word = random.choice(words)
        if len(password + word) <= length:
            password += word.capitalize()
        else:
            break
        if len(password) < length:
            password += random.choice(string.digits + symbols)
    password = ''.join(random.sample(password, len(password)))
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
app.geometry("600x200")
app.config(bg='black')
app.title("Louitron's Password Generator - Made with Python!")

strength = tk.StringVar()

style = ttk.Style()
style.configure("My.TFrame", background="#808080")
style.configure("My.TRadiobutton", background="#808080", foreground="#000000")
style.configure("My.TLabel", background="#808080", foreground="#000000")

frame = ttk.Frame(app, padding="30 15 30 15", style="My.TFrame")
frame.pack(fill='both', expand=True)

strength_label = ttk.Label(frame, text="Password Strength:", font=("TkDefaultFont", 12), style="My.TLabel")
strength_label.grid(column=0, row=1, sticky="W")

user_message = ttk.Label(frame, text="Hello There! Please select the strength of your password and click 'generate'.", font=("TkDefaultFont", 12), style="My.TLabel")
user_message.grid(column=0, row=0, sticky="W", columnspan=4)

strong_radio = ttk.Radiobutton(frame, text="Strong", variable=strength, value="strong", style="My.TRadiobutton")
strong_radio.grid(column=0, row=2, sticky="W")

medium_radio = ttk.Radiobutton(frame, text="Medium", variable=strength, value="medium", style="My.TRadiobutton")
medium_radio.grid(column=1, row=2, sticky="W")

easy_radio = ttk.Radiobutton(frame, text="Easy", variable=strength, value="easy", style="My.TRadiobutton")
easy_radio.grid(column=2, row=2, sticky="W")

generate_button = ttk.Button(frame, text="Generate", command=generate_button_clicked, style="My.TButton")
generate_button.grid(column=1, row=3, sticky="W")

password_output = tk.Label(app, text="Your Password Will Appear Here, Click To Copy", font=("TkDefaultFont", 14), bg='black', fg='gray')
password_output.pack()

app.mainloop()
