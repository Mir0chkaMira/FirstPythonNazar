import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Game")
root.geometry("600x600+700+300")


label = tk.Label(text="Guess the number",
                 font=("Arial", 18))


def random_number():
    global random_number

    random_number = randint(1, 100)
    number_entry.delete(0, tk.END)

    label.config(text="I chose my number")
    random_button.pack_forget()


def guess_number():
    global random_number

    choice = int(number_entry.get())

    if choice < random_number:
        label.config(text="My number is bigger")
    elif choice > random_number:
        label.config(text="My number is lower")
    else:
        label.config(text=f"You guessed it! {random_number} was my number!")


number_entry = tk.Entry(font=("Arial", 18))

random_button = tk.Button(text="Random number",
                          bg="black",
                          fg="white",
                          width=15,
                          font=("Comic Sans MS", 20),
                          command=random_number)

guess_button = tk.Button(text="Guess",
                         bg="black",
                         fg="white",
                         width=15,
                         font=("Comic Sans MS", 20),
                         command=guess_number)

label.pack()
number_entry.pack()
guess_button.pack()
random_button.pack()
root.mainloop()
