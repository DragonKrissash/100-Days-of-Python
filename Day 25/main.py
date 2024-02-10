import turtle
import pandas as pd
screen=turtle.Screen()
screen.title('U.S. States Games')
img='blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
df=pd.read_csv('50_states.csv')
states=list(df['state'])
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
state_counter=turtle.Turtle()
state_counter.penup()
state_counter.hideturtle()
state_count=0

def showState(state):
    df_ans = df[df['state'] == state]
    x = int(df_ans.x)
    y = int(df_ans.y)
    tim.goto(x=x, y=y)
    tim.write(state, move=False, align='center', font=('Arial', 8, 'normal'))

def addStateCount(count):
    state_counter.goto(150,200)
    state_counter.clear()
    state_counter.write(f'{count}/50',move=False,align='center',font=('Arial', 8, 'normal'))

for i in range(50):
    addStateCount(state_count)
    state=screen.textinput(title='Guess the state',prompt="What's another state's name?")
    if state==None:
        break
    if(state in states):
        showState(state)
        state_count+=1
        addStateCount(state_count)
turtle.mainloop()