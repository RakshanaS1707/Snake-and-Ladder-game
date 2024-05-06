import tkinter as tk
from PIL import ImageTk,Image
import random

def start_game():
    global img2,b1,b2
    #buttons for players
    #player1
    b1.place(x=1100,y=400)

    #player2
    b2.place(x=1100,y=550)

    #dice
    img2=Image.open("roll.png")
    img2=img2.resize((80,80))
    img2=ImageTk.PhotoImage(img2)
    b3=tk.Button(root,image=img2,height=80,width=80)
    b3.place(x=1170,y=150)

    #exit button
    b4=tk.Button(root,text="END GAME",height=3,width=17,fg="black",bg="red",font=('Cursive',14,'bold'),activebackground='yellow',command=root.destroy)
    b4.place(x=1100,y=20)

def reset_coins():
    global player_1,player_2,pos1,pos2

    player_1.place(x=0,y=750)
    player_2.place(x=50,y=750)

    pos1=0
    pos2=0

def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for name in names:
        img3=Image.open(name)
        img3=img3.resize((80,80))
        img3=ImageTk.PhotoImage(img3)
        Dice.append(img3)

def check_Ladder(Turn):
    global pos1,pos2,Ladder

    f=0 # No ladder
    if Turn==1:
        if pos1 in Ladder.keys():
            pos1=Ladder[pos1]
            f=1
        else:
            if pos2 in Ladder.keys():
                pos2=Ladder[pos2]
                f=1
        return f

def check_Snake(Turn):
    global pos1,pos2

    if Turn==1:
        if pos1 in Snake.keys():
            pos1=Snake[pos1]
    else:
        if pos2 in Snake.keys():
            pos2=Snake[pos2]

def roll_dice():
    global Dice,turn,pos1,pos2,b1,b2
    
    r=random.randint(1,6)
    b3=tk.Button(root,image=Dice[r-1],height=80,width=80)
    b3.place(x=1170,y=150)

    Lad=0
    if turn==1:
        if (pos1+r)<=100:
            pos1=pos1+r
        Lad=check_Ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos1)
        if r!=6 and Lad!=1:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2+r)<=100:
            pos2=pos2+r
        Lad=check_Ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos2)
        if r!=6 and Lad!=1:
            turn=1
            b2.configure(state='disabled')
            b1.configure(state='normal')

    is_winner()

def is_winner():
    global pos1,pos2

    if pos1==100:
        msg="PLAYER 1 is the Winner"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg="red",font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
        msg="PLAYER 2 is the Winner"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg="red",font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
        

def move_coin(Turn,r):
    global player_1,player_2
    global Index

    if Turn==1:
        player_1.place(x=Index[r][0],y=Index[r][1])
    else:
        player_2.place(x=Index[r][0],y=Index[r][1])

def get_Index():
    global player_1,player_2
    Num = [100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    row=-10
    i=0
    for x in range(1,11):
        col=20
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            col=col+101
            i=i+1
        row=row+81
    
    '''player_1.place(x=40,y=20)
    player_2.place(x=40,y=20)
    row=20
    col=40'''
 

#to store dice images
Dice=[]

#to store x,y coordinates of given number
Index={}

#initial positions of players
pos1=None
pos2=None

#ladder bottom to top
Ladder={8:29,19:57,26:45,46:97,50:69,60:79,73:92}

#snake head to tail
Snake={99:43,94:66,85:55,70:13,63:25,48:6,39:3}

#create GUI window
root=tk.Tk()
root.geometry("1200x800")#window size
root.title("Snakes and Ladders")

F1=tk.Frame(root,width=1200,height=800,relief='raised')
F1.place(x=10,y=10)

#set board
img1=ImageTk.PhotoImage(Image.open("board.png"))
Lab=tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

#player1 button
b1=tk.Button(root,text="PLAYER 1",height=3,width=17,fg="black",bg="orange",font=('Cursive',14,'bold'),activebackground='yellow',command=roll_dice)
#player2 button
b2=tk.Button(root,text="PLAYER 2",height=3,width=17,fg="black",bg="cyan",font=('Cursive',14,'bold'),activebackground='yellow',command=roll_dice)


#player1-coin
player_1=tk.Canvas(root,width=40,height=40)
player_1.create_oval(10,10,40,40,fill='orange')

#player2-coin
player_2=tk.Canvas(root,width=40,height=40)
player_2.create_oval(10,10,40,40,fill='cyan')

#whose turn first - by default player1
turn=1

#keep coins at initial positions
reset_coins()

#get index of each num
get_Index()

#load dice images
load_dice_images()

start_game()

root.mainloop()#keep on running until closed
