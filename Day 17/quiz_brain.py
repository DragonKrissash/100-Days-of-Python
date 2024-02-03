class QuizBrain():
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        question=self.question_list[self.question_number]
        ans=input(f'Q.{self.question_number+1}: {question.text} (True/False) :')
        self.check_answer(ans,question.answer)

    def check_answer(self,ans,cor_ans):
        if ans.lower()==cor_ans.lower():
            print("It's correct answer!")
            self.score+=1
        else:
            print("It's wrong answer!")
        print('The correct answer was: ',cor_ans)
        print(f'Your score is: {self.score}/{self.question_number+1}')
        self.question_number += 1
        print('\n')