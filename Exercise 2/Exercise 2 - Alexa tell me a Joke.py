import tkinter as tk
import random

def load_jokes():
    jokes = []
    try:
        with open("randomJokes.txt", "r", encoding="utf-8") as file:
            for line in file:
                if "?" in line:
                    setup, punchline = line.strip().split("?", 1)
                    jokes.append((setup + "?", punchline))
    except FileNotFoundError:
        jokes = [("Error: randomJokes.txt not found!", "Please add the file and try again.")]
    return jokes


def show_joke():
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0])
    punchline_label.config(text="")
    show_punchline_button.config(state="normal")


def show_punchline():
    punchline_label.config(text=current_joke[1])
    show_punchline_button.config(state="disabled")

root = tk.Tk()
root.title("Alexa Joke Assistant")
root.geometry("500x300")

jokes = load_jokes()
current_joke = None

title_label = tk.Label(root, text="Alexa Joke Assistant", font=("Arial", 20))
title_label.pack(pady=10)

tell_button = tk.Button(root, text="Alexa tell me a Joke", font=("Arial", 14), command=show_joke)
tell_button.pack(pady=10)

setup_label = tk.Label(root, text="", font=("Arial", 14))
setup_label.pack(pady=10)

show_punchline_button = tk.Button(root, text="Show Punchline", font=("Arial", 12), command=show_punchline)
show_punchline_button.pack(pady=5)
show_punchline_button.config(state="disabled")

punchline_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
punchline_label.pack(pady=5)

next_button = tk.Button(root, text="Next Joke", font=("Arial", 12), command=show_joke)
next_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=root.destroy)
quit_button.pack(pady=10)

root.mainloop()
