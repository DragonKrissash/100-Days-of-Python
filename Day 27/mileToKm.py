from tkinter import *
window=Tk()
window.title('Mile to KM convertor')
window.config(padx=50,pady=50)
#labels

miles=Label(text='Miles',font=('Arial',12,'bold'))
miles.grid(row=1,column=3)
km=Label(text='KM',font=('Arial',12,'bold'))
km.grid(row=2,column=3)
is_equal=Label(text='is equal to: ',font=('Arial',12,'bold'))
is_equal.grid(row=2,column=1)
ans=Label(text="0",font=('Arial',12,'bold'))
ans.grid(row=2,column=2)

#button
def convToKm():
    num=input.get()
    num_km=int(num)*1.6
    ans.config(text=f'{num_km}')

button=Button(text="Calculate",command=convToKm)
button.grid(row=3,column=2)



#entry
input=Entry(width=10)
input.grid(row=1,column=2)


window.mainloop()