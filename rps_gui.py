from tkinter import *
from PIL import ImageTk,Image
#display
root=Tk()
rock_img=ImageTk.PhotoImage(Image.open('rock.png').resize((50,50)))
scissor_img = ImageTk.PhotoImage(Image.open('scissor.png').resize((50,50)))
paper_img = ImageTk.PhotoImage(Image.open('paper.png').resize((50,50)))
ROCK_BUTTON=Button(root,image=rock_img)
ROCK_BUTTON.grid(row=1,column=0)
PAPER_BUTTON=Button(image=paper_img)
PAPER_BUTTON.grid(row=1,column=1)
SCISSOR_BUTTON=Button(image=scissor_img)
SCISSOR_BUTTON.grid(row=1,column=2)
SCOREBOARD=Label(root,text='SCORES')
SCOREBOARD.grid(row=0,column=0,columnspan=3)

root.mainloop()