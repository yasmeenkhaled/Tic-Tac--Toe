from glob import glob
from tkinter import *
import random


def next_turn(row, col):
    global player
    if game_botns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            
            game_botns[row][col]['text'] = player

            if check_winner() == False:
                
                player = players[1]
                label.config(text=(players[1] + " Turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text=("!!! No Winner !!!"))

        elif player == players[1]:
            
            game_botns[row][col]['text'] = player

            if check_winner() == False:
                
                player = players[0]
                label.config(text=(players[0] + " Turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text=("!!! No Winner !!!"))


def check_winner():
    
    for row in range(3):
        if game_botns[row][0]['text'] == game_botns[row][1]['text'] == game_botns[row][2]['text'] != "":
            game_botns[row][0].config(bg="#778899")
            game_botns[row][1].config(bg="#778899")
            game_botns[row][2].config(bg="#778899")
            return True

    
    for col in range(3):
        if game_botns[0][col]['text'] == game_botns[1][col]['text'] == game_botns[2][col]['text'] != "":
            game_botns[0][col].config(bg="#778899")
            game_botns[1][col].config(bg="#778899")
            game_botns[2][col].config(bg="#778899")
            return True

    
    if game_botns[0][0]['text'] == game_botns[1][1]['text'] == game_botns[2][2]['text'] != "":
        game_botns[0][0].config(bg="#778899")
        game_botns[1][1].config(bg="#778899")
        game_botns[2][2].config(bg="#778899")
        return True
    elif game_botns[0][2]['text'] == game_botns[1][1]['text'] == game_botns[2][0]['text'] != "":
        game_botns[0][2].config(bg="#778899")
        game_botns[1][1].config(bg="#778899")
        game_botns[2][0].config(bg="#778899")
        return True

    
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_botns[row][col].config(bg="#ffc0cb")

        return 'tie'

    else:
        return False
 

def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_botns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = random.choice(players)

    label.config(text=(player + " Turn"))

    for row in range(3):
        for col in range(3):
            game_botns[row][col].config(text="", bg="#87CEEB")


window = Tk()
window.title("Tic-Tac-Toe [X - O]")
window.configure(bg="#87CEEB")

players = ["x", "o"]
player = random.choice(players)

game_botns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


label = Label(text=(player + " Turn"), font=('consolas', 50))
label.configure(bg="#87CEEB",fg="#ffffff")
label.pack(side="top")

restart_botn = Button(text="Restart",bd=15,fg="#FFFFFF", font=('consolas', 15), command=start_new_game)
restart_botn.pack(side="bottom")
restart_botn.configure(bg="#778899")

botns_frame = Frame(window)
botns_frame.pack()


for row in range(3):
    for col in range(3):
        game_botns[row][col] = Button(botns_frame,bd=10, text="", font=('consolas', 60),fg="#ffffff",background=("#87CEEB"), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_botns[row][col].grid(row=row , column=col)

window.mainloop()
