# URL - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#solution
def turn_right():
    for i in range(0,3):
        turn_left()
def move_front():
     while front_is_clear():
            move()

def check_right():
    if right_is_clear():
        turn_right()
           
def check_end():
    if not front_is_clear():
        if not right_is_clear():
            turn_left()
            if front_is_clear():
                move()
            else:
                turn_left()
                move()
                turn_right()
                move()
    
while not at_goal():
    check_right()
    move_front()
    check_end() 
    