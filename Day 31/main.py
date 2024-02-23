BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from datafile import data_file
import random as rd
window=Tk()
window.title('Flash Card!')
window.config(padx=50,pady=50,bg="#B1DDC6")


def showAnswer():
    canvas.create_image(400,263,image=back_img)
    lang.config(text='English',bg="#B1DDC6",font=('Ariel',40,'italic'))
    text = rd.choice(data_file['English'])
    word.config(text=text,bg="#B1DDC6",font=('Ariel',60,'bold'))


def startAgain():
    canvas.create_image(400,263,image=front_img)
    lang.config(text='French',bg='white',font=('Ariel',40,'italic'))
    text=rd.choice(data_file['French'])
    word.config(text=text,bg='white',font=('Ariel',60,'bold'))
    window.after(3000,showAnswer)



canvas=Canvas(width=800,height=526,bg="#B1DDC6",highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
front_img=PhotoImage(file='./images/card_front.png')
back_img=PhotoImage(file='./images/card_back.png')

lang=Label(text='French',font=('Ariel',40,'italic'),bg='#B1DDC6')
lang.place(x=320,y=120)

word=Label(text='trouve',font=('Ariel',60,'bold'),bg='#B1DDC6')
word.place(x=280,y=210)

tick_img=PhotoImage(file='./images/right.png')
cross_img=PhotoImage(file='./images/wrong.png')

tick=Button(image=tick_img,highlightthickness=0,command=startAgain)
tick.grid(row=1,column=1)

cross=Button(image=cross_img,highlightthickness=0,command=startAgain)
cross.grid(row=1,column=0)






window.mainloop()
