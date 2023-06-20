import tkinter as tk
import random


def RPS(choice):
    botChoice = random.choice(["Rock", "Paper", "Scissors"])
    if choice == botChoice:
        result = "Draw !"
    elif (choice == "Rock" and botChoice == "Scissors") or (choice == "Paper" and botChoice == "Rock") or (
            choice == "Scissors" and botChoice == "Paper"):
        result = "Player wins !"
    else:
        result = "Bot wins !"

    result_label.config(text="Player: {}  Bot: {}\n{}".format(choice, botChoice, result))


window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x300")

instruction_label = tk.Label(window, text="Choose :")
instruction_label.pack()

button_rock = tk.Button(window, text="Rock", command=lambda: RPS("Rock"))
button_rock.pack()

button_paper = tk.Button(window, text="Paper", command=lambda: RPS("Paper"))
button_paper.pack()

button_scissors = tk.Button(window, text="Scissors", command=lambda: RPS("Scissors"))
button_scissors.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
