import tkinter as tk
from PIL import ImageTk,Image
from random import randint

font = 'Microsoft'
background = 'pink'


window = tk.Tk()
photo = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/RPS.png"))
window.iconphoto(False,photo)
window.title('Rock,Paper,Scissors Game')
window.configure(bg=background)


# Getting Pictures
user_rock_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/user-rock.png"))
user_paper_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/user-paper.png"))
user_scissors_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/user-scissors.png"))
ai_rock_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/ai-rock.png"))
ai_paper_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/ai-paper.png"))
ai_scissors_pic = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/ai-scissors.png"))


# Label Rock,Paper,Scissors
rock_paper_scissors_lbl = tk.Label(window,text='Rock,Paper,Scissors Game',font=(font,15,'bold'),bg=background)
rock_paper_scissors_lbl.grid(row=0,column=2)


# insert pictures
user_pic_lbl = tk.Label(window,image=user_rock_pic,)
ai_pic_lbl = tk.Label(window,image=ai_rock_pic,)

user_pic_lbl.grid(row=1,column=4)
ai_pic_lbl.grid(row=1,column=0)


# indicators
user_lbl = tk.Label(window,text='You',font=(font,12,'bold'),bg=background)
ai_lbl = tk.Label(window,text='Computer',font=(font,12,'bold'),bg=background)

user_lbl.grid(row=0,column=4)
ai_lbl.grid(row=0,column=0)


# VS label
vs_lbl = tk.Label(window,text='VS',font=(font,14,'bold'),bg=background)
vs_lbl.grid(row=1,column=2)


# Score label
user_score_lbl = tk.Label(window,text='0',font=(font,13,'bold'),bg=background)
ai_score_lbl = tk.Label(window,text='0',font=(font,13,'bold'),bg=background)

user_score_lbl.grid(row=1,column=3,padx=(0,35))
ai_score_lbl.grid(row=1,column=1,padx=(35,0))


# Risult Game
risult_game = tk.Label(window,text='Risult...',font=(font,12,'bold'),bg=background)
risult_game.grid(row=1,column=2,pady=(150,0))


# Reset btn 
def reset_btn():
    user_score_lbl['text'] = '0'
    ai_score_lbl['text'] = '0'
    risult_game['text'] = 'Risult...'

reset_btn = tk.Button(window,text='Reset Game',width=15,font=(font,12,'bold'),bg='black',fg='white',
command=reset_btn)
reset_btn.grid(row=1,column=2,pady=(0,150))


# Update pictures 
def update_pictures(user_input):
    # for user
    if user_input == 'Rock':
        user_pic_lbl['image'] = user_rock_pic
    elif user_input == 'Paper':
        user_pic_lbl['image'] = user_paper_pic
    elif user_input == 'Scissors':
        user_pic_lbl['image'] = user_scissors_pic

    # for AI
    choices = ['Rock','Paper','Scissors']
    choice = choices[randint(0,2)]
    if choice == 'Rock':
        ai_pic_lbl['image'] = ai_rock_pic
    elif choice == 'Paper':
        ai_pic_lbl['image'] = ai_paper_pic
    elif choice == 'Scissors':
        ai_pic_lbl['image'] = ai_scissors_pic

    check_winner(user_input,choice)


def check_winner(player,computer):
    if player == computer:
        risult_game['text'] = 'TIE!'
    elif player == 'Rock' and computer == 'Scissors':
        update_message()
        update_user_score()
    elif player == 'Paper' and computer == 'Rock':
        update_message()
        update_user_score()
    elif player == 'Scissors' and computer == 'Paper':
        update_message()
        update_user_score()
    else:
        risult_game['text'] = 'YOU LOSE!'
        update_ai_score()


# Update message
def update_message():
    risult_game['text'] = 'YOU WON'

# Update user score 
def update_user_score():
    score = int(user_score_lbl['text'])
    score += 1
    user_score_lbl['text'] = str(score)

# Update ai score
def update_ai_score():
    score = int(ai_score_lbl['text'])
    score += 1
    ai_score_lbl['text'] = str(score)


# Rock btn
rock_btn = tk.Button(window,text='Rock',width=15,font=(font,12,'bold'),bg='limegreen',
command=lambda:update_pictures('Rock'))
rock_btn.grid(row=2,column=1)


# Paper btn 
paper_btn = tk.Button(window,text='Paper',width=15,font=(font,12,'bold'),
command=lambda:update_pictures('Paper'))
paper_btn.grid(row=2,column=2)


# Scissors btn
scissors_btn = tk.Button(window,text='Scissors',width=15,font=(font,12,'bold'),bg='hotpink',
command=lambda:update_pictures('Scissors'))
scissors_btn.grid(row=2,column=3)


window.mainloop()