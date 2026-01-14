from tkinter import *
from tkinter import messagebox

#fucntion to put X and O in box
x_win=0
o_win=0
draw=0
clicked =False
count =0
def click(b):
    global clicked,count
    if b['text']==' ' and clicked==False:
        b['text']="X"
        count+=1
        clicked=True
        check_winner()
    elif b['text']==' ' and clicked==True:
        b['text']="O"
        count+=1
        clicked=False
        check_winner()
    else:
        messagebox.showerror("Error!!","Hey, can't enter here!!")

#to disable all buttons after someone won
def disable_all_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

#to check if X won

def check_winner():
    global winner,x_win,o_win,draw
    winner = "Draw"
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
        button1.config(bg="#ffb6be")
        button2.config(bg="#ffb6be")
        button3.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
        button4.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button6.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X":
        button7.config(bg="#ffb6be")
        button8.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
        button1.config(bg="#ffb6be")
        button4.config(bg="#ffb6be")
        button7.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
        button2.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button8.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
        button3.config(bg="#ffb6be")
        button6.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
        button1.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()
    elif button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
        button3.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button7.config(bg="#ffb6be")
        winner = "X"
        messagebox.showinfo("Winner", "X wins the game!! 🎉")
        disable_all_buttons()

#to check if O won

    if button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O":
        button1.config(bg="#ffb6be")
        button2.config(bg="#ffb6be")
        button3.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O":
        button4.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button6.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O":
        button7.config(bg="#ffb6be")
        button8.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O":
        button1.config(bg="#ffb6be")
        button4.config(bg="#ffb6be")
        button7.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O":
        button2.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button8.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O":
        button3.config(bg="#ffb6be")
        button6.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    if button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O":
        button1.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button9.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()
    elif button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O":
        button3.config(bg="#ffb6be")
        button5.config(bg="#ffb6be")
        button7.config(bg="#ffb6be")
        winner = "O"
        messagebox.showinfo("Winner", "O wins the game!! 🎉")
        disable_all_buttons()

# check for draw and increase win count
    if winner=="X":
        x_win+=1
        win_loss()
    elif winner=="O":
        o_win+=1
        win_loss()
    if count==9 and winner =="Draw":
        draw+=1
        win_loss()
        messagebox.showinfo("Draw", "It's a draw! 🤝")
        disable_all_buttons()
        
    
    
window = Tk()
window.geometry("600x600")
window.title("Tic-Tac-Toe")
window.config(background="orange",)
frame1=Frame(window)
Label(frame1,text="Tic Tac Toe",font=("impact","45"),bg="orange",fg="black").pack()
frame1.pack()

frame2=Frame(window)
frame2.pack()

frame3=Frame(window)
frame3.pack()

label3 = Label(frame3, text="X win: 0   O win: 0   Draw: 0",font=("impact","25"),bg="orange",fg="black")
label3.pack()

#win loss count
def win_loss():
    
    label3.config(text=f"X win: {x_win}   O win: {o_win}   Draw: {draw}")



# making tic tac toe box
def reset():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    global clicked,count
    clicked = True
    count = 0
    button1 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button1),bg="yellow",relief=RAISED,borderwidth=5)
    button1.grid(row=0,column=0)
    button2 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button2),bg="yellow",relief=RAISED,borderwidth=5)
    button2.grid(row=0,column=1)
    button3 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button3),bg="yellow",relief=RAISED,borderwidth=5)
    button3.grid(row=0,column=2)

    button4 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button4),bg="yellow",relief=RAISED,borderwidth=5)
    button4.grid(row=1,column=0)
    button5 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button5),bg="yellow",relief=RAISED,borderwidth=5)
    button5.grid(row=1,column=1)
    button6 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button6),bg="yellow",relief=RAISED,borderwidth=5)
    button6.grid(row=1,column=2)

    button7 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button7),bg="yellow",relief=RAISED,borderwidth=5)
    button7.grid(row=2,column=0)
    button8 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button8),bg="yellow",relief=RAISED,borderwidth=5)
    button8.grid(row=2,column=1)
    button9 = Button(frame2,text=' ',width=4,height=2,font=("Aerial","30"),command=lambda:click(button9),bg="yellow",relief=RAISED,borderwidth=5)
    button9.grid(row=2,column=2)

#to start the game
reset()

#to create menu
my_menu=Menu(window)
window.config(menu=my_menu)

#to add menu option
options_menu= Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset game",command=reset)


window.mainloop()