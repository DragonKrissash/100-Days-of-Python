from tkinter import Entry, Button, Tk, Label

import tkinter

from tkinter import *
window=Tk()
window.title('My first gui')
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label

my_label=Label(text='I am a label',font=('Arial',24,'bold'))
my_label.grid(row=1,column=1)
my_label['text']='new text'
my_label.config(text='new text')

#Button
def button_click():
    print('I got clicked')
    new_text=input.get()
    my_label.config(text=new_text)

button=Button(text='Click me',command=button_click)
button.grid(row=2,column=2)

b2=Button(text='Button 2')
b2.grid(row=1,column=3)
#Entry

input=Entry(width=10)
input.grid(row=3,column=4)


window.mainloop()