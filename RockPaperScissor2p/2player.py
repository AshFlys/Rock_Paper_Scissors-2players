
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from random import randint


# main window
root = tkinter.Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/humRock.png"))
paper_img = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/humPaper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/humanSci.png"))
rock_img_p2 = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/hum2Rock.png"))
paper_img_p2 = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/hum2Paper.png"))
scissor_img_p2 = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/hum2Sci.png"))
Player1_Wins_img = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/player1wins.png"))
Player2_Wins_img = ImageTk.PhotoImage(Image.open("RockPaperScissor2P/player2wins.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
user_label.grid(row=1, column=4)
p2_label = Label(root, image=scissor_img_p2, bg="#9b59b6")
p2_label.grid(row=1, column=0)


# scores
playerScore = Label(root, font=50, text=0, bg="#9b59b6", fg="white")
player2Score = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
player2Score.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
p1_indicator =  Label(root, font=50, text="Player 1", bg="#9b59b6", fg="white")
p2_indicator = Label(root, font = 50, text="Player 2",  bg="#9b59b6", fg="white")
p1_indicator.grid(row=0, column=3)
p2_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg ['text'] = x

#final result

def finalResult(winner):
    if winner == "human":
        destroyLabels()
        user_label = Label(root, image=Player1_Wins_img, bg="#9b59b6")
        user_label.grid(row=0, column=0)

    elif winner == "player2":
        destroyLabels()
        user_label = Label(root, image=Player2_Wins_img, bg="#9b59b6")
        user_label.grid(row=0, column=0)

# destroy labels

def destroyLabels():
    user_label.destroy() 
    p2_label.destroy() 
    player2Score.destroy()
    playerScore.destroy()
    p1_indicator.destroy()
    p2_indicator.destroy()
    msg.destroy()
    rock.grid_forget()
    paper.grid_forget()
    scissor.grid_forget()

# update human score
def UpdateHumanScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    if score == 5:
        finalResult("human")

# update computer score
def UpdatePlayer2Score():
    score = int(player2Score["text"])
    score += 1
    player2Score["text"] = str(score)
    if score == 5:
        finalResult("player2")

#winner
def checkWin(player, player2):
    if player == player2:
        updateMessage("it is a tie")
        pass
    elif player == "rock":
        if player2 == "paper":
         updateMessage ("You have lost")
         UpdatePlayer2Score()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass
    elif player == "paper":
        if player2 == "scissor":
         updateMessage ("You have lost")
         UpdatePlayer2Score()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass
    elif player == "scissor":
        if player2 == "rock":
         updateMessage ("You have lost")
         UpdatePlayer2Score()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass

def updateplayer1Choice(X):
        if X == "rock":
            user_label.configure(image=rock_img)
            checkWin(X, Y)
        elif X == "paper":
            user_label.configure(image=paper_img)
            checkWin(X, Y)
        else:
            user_label.configure(image=scissor_img)
            checkWin(X, Y)
      
def updateplayer2Choice(Y):
        if  Y== "rock":
            p2_label.configure(image=rock_img_p2)
            checkWin(X, Y)
        elif Y == "paper":
            p2_label.configure(image=paper_img_p2)
            checkWin(X, Y)
        else:
            p2_label.configure(image=scissor_img_p2)
            checkWin(X, Y)
    




#buttons
#lamda is an anonymous function that allows you to add another fucntion
rock = tkinter.Button(root, width=20, height=2, text="ROCK 2", bg="#FF3E4D", fg="white", command=lambda: updateplayer1Choice("rock"))
rock.grid(row=3, column=1)

rock = tkinter.Button(root, width=20, height=2, text="ROCK 1", bg="#FF3E4D", fg="white", command=lambda: updateplayer2Choice("rock"))
rock.grid(row=2, column=1)

paper = tkinter.Button(root, width=20, height=2, text="PAPER 2 ", bg="#FAD02E", fg="white", command=lambda: updateplayer1Choice("paper"))
paper.grid(row=3, column=2)

paper = tkinter.Button(root, width=20, height=2, text="PAPER 1", bg="#FAD02E", fg="white", command=lambda: updateplayer2Choice("paper"))
paper.grid(row=2, column=2)

scissor = tkinter.Button(root, width=20, height=2, text="SCISSOR 2", bg="#0ABDE3", fg="white", command=lambda: updateplayer1Choice("scissor"))
scissor.grid(row=3, column=3)

scissor = tkinter.Button(root, width=20, height=2, text="SCISSOR 1", bg="#0ABDE3", fg="white", command=lambda: updateplayer2Choice("scissor"))
scissor.grid(row=2, column=3)


root.mainloop()