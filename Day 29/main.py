from tkinter import *
from tkinter import messagebox
import passw
import pyperclip
window=Tk()
window.title("Password Generator")
window.config(pady=50,padx=50)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGen():
    passkey=passw.genPassword()
    password_entry.delete(0,END)
    password_entry.insert(0,passkey)
    pyperclip.copy(passkey)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    web_text=web_entry.get()
    email_text=email_entry.get()
    password_text=password_entry.get()

    if len(web_text)==0 or len(password_text)==0:
        messagebox.showinfo(title='Error',message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=web_text,message=f'These are the details entered: \nEmail: {email_text} \nPassword: {password_text} \nWebsite: {web_text} \nIs it okay to save?')

        if is_ok:
            with open('data.txt','a') as file:
                file.write(f'{web_text} | {email_text} | {password_text}\n')
                web_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


canvas=Canvas(width=200,height=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

web=Label(text="Website:")
web.grid(row=1,column=0)

email=Label(text='Email/Username:')
email.grid(row=2,column=0)

password=Label(text='Password:')
password.grid(row=3,column=0)

web_entry=Entry(width=40)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'kishore@gmail.com')

password_entry=Entry(width=22)
password_entry.grid(row=3,column=1)

gen_pass=Button(text='Generate Password',command=passwordGen)
gen_pass.grid(row=3,column=2)

add=Button(text='Add',width=34,command=saveData)
add.grid(row=4,column=1,columnspan=2)



window.mainloop()