from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.x=0
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle('square');
            segment.color('white')
            segment.penup()
            segment.goto(x=self.x, y=0)
            self.segments.append(segment)
            self.x-=20
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x=self.segments[seg_num-1].xcor()
            y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=x,y=y)
        self.head.forward(20)

    def addSegment(self,position):
        segment = Turtle('square');
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def up(self):
        if self.head.heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)
