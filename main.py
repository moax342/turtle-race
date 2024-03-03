from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() -10
    tim.setheading(new_heading)

def clear_sc():
    tim.clear()


sc = Screen()
sc.listen()


sc.onkey(key="Up",fun=move_forward)
sc.onkey(key="Down",fun=move_backwards)
sc.onkey(key="Right",fun=counter_clockwise)
sc.onkey(key="Left",fun=clockwise)
sc.onkey(key="c",fun=clear_sc)

sc.exitonclick()
