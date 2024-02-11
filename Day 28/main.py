from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
time=None
checkmark=''
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time)
    global reps
    reps=0
    canvas.itemconfig(timer_text, text=f'00:00')
    timer.config(text='Timer')
    global checkmark
    checkmark=''
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps in (1,3,5,7):
        timer.config(text='Work Min')
        count_down(60*WORK_MIN)
    if reps in (2,4,6):
        timer.config(text='Short Break')
        count_down(60*SHORT_BREAK_MIN)
    if reps==8:
        timer.config(text='Long Break')
        count_down(60*LONG_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global checkmark
    min=count//60
    sec=count%60
    if min//10==0:
        min='0'+str(min)
    if sec//10==0:
        sec='0'+str(sec)
    canvas.itemconfig(timer_text,text=f'{min}:{sec}')
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()
        global checkmark
        checkmark = ''
        for i in range(reps//2):
            checkmark+='✔'
        check.config(text=checkmark)



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)



canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(102,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=2,column=2)

timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,'bold'),bg=YELLOW)
timer.grid(row=1,column=2)
check=Label(fg=GREEN,font=(FONT_NAME,20),bg=YELLOW)
check.grid(row=4,column=2)
start=Button(text='Start',bg='white',fg='black',font=('Arial',12),highlightthickness=0,command=start_timer)
start.grid(row=3,column=1)

reset=Button(text='Reset',bg='white',fg='black',font=('Arial',12),highlightthickness=0,command=reset_timer)
reset.grid(row=3,column=3)

window.mainloop()