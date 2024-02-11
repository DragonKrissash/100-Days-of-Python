import json
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
    new_data={
        web_text:{
            'email':email_text,
            'password':password_text
        }
    }
    if len(web_text)==0 or len(password_text)==0:
        messagebox.showinfo(title='Error',message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json','r') as data_file:
                data=json.load(data_file)
        except:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json','w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)

def displayDetails():
    website=web_entry.get()
    try:
        with open('data.json','r')as data_file:
            data=json.load(data_file)
            if website in data.keys():
                email=data[website]['email']
                passkey=data[website]['password']
                messagebox.showinfo(title='Details',message=f'Email: {email}\nPassword: {passkey}')
            else:
                messagebox.showinfo(title='Error',message='There is no website with the name '+website)
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='There is no data to search!\nPlease submit some data first!')


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

web_entry=Entry(width=22)
web_entry.grid(row=1,column=1)
web_entry.focus()

email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'kishore@gmail.com')

password_entry=Entry(width=22)
password_entry.grid(row=3,column=1)

search=Button(text="Search",command=displayDetails)
search.grid(row=1,column=2)
gen_pass=Button(text='Generate Password',command=passwordGen)
gen_pass.grid(row=3,column=2)

add=Button(text='Add',width=34,command=saveData)
add.grid(row=4,column=1,columnspan=2)



window.mainloop()