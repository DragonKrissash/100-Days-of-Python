from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=50,pady=50)
        self.score=Label(text='Score: 0',fg='white',padx=20,pady=20,bg=THEME_COLOR)
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(width=400,height=350,bg='white')
        self.question_text=self.canvas.create_text(200,170,width=350,text='HI',fill='black',font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        tick_img=PhotoImage(file='./images/true.png')
        cross_img=PhotoImage(file='./images/false.png')
        self.tick=Button(image=tick_img,highlightthickness=0,padx=20,pady=20,command=self.true_pressed)
        self.tick.grid(row=2,column=0)
        self.cross = Button(image=cross_img, highlightthickness=0,padx=20,pady=20,command=self.false_pressed)
        self.cross.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='You have reached the end of quiz!')
            self.tick.config(state='disabled')
            self.cross.config(state='disabled')
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if (is_right):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)

