from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] != "" or check_winner() is True:
        return

    elif player == players[0]:
        buttons[row][column]['text'] = player

    elif player == players[1]:
        buttons[row][column]['text'] = player

    switch_turns()


def switch_turns():
    global player

    if check_winner() is True or check_winner() == "Tie":
        print_winner()
        return

    if player == players[0]:
        player = players[1]
        label.config(text=f"Current turn: {player}")

    elif player == players[1]:
        player = players[0]
        label.config(text=f"Current turn: {player}")


def print_winner():
    global player

    if check_winner() == "Tie":
        label.config(text="It's a tie!")
        return

    label.config(text=f"{player} won!")


def check_winner():
    for i in range(0, 3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            buttons[0][i].config(bg="green")
            buttons[1][i].config(bg="green")
            buttons[2][i].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    if empty_spaces() is False:
        for row in range(0, 3):
            for column in range(0 ,3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    return False


def empty_spaces():
    spaces = 9

    for row in range(0, 3):
        for column in range(0, 3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=f"Current turn: {player}")

    for row in range(0, 3):
        for column in range(0, 3):
            buttons[row][column].config(text="", bg="#F0F0F0")


root = Tk()

root.title('Tic Tac Toe')
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=f"Current turn: {player}", font=("Consolas", 40))
label.pack(side=TOP)

reset_button = Button(text="Restart", font=("Consolas", 20), command=new_game)
reset_button.pack(side=TOP)

frame = Frame(root)
frame.pack()

for row in range(0, 3):
    for column in range(0, 3):
        buttons[row][column] = Button(frame, text="",
                                      font=("Consolas", 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)


root.mainloop()
