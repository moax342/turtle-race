from turtle import Turtle,Screen
import random

sc = Screen()
sc.title("Turtle Race")
sc.setup(height=400,width=500)
is_race_on = False

user_bet= sc.textinput(title="Choose A warrior",prompt="Enter your warrior color")
colors=["red","green","yellow","orange","blue","Black"]
y_pos=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_turt=turtle.pencolor()
            if winning_turt==user_bet:
                print(f"you Won the {winning_turt} is the wining turtle")
            else:
                print(f"You lost the {winning_turt} is the wining turtle ")
        distance= random.randint(0,11)
        turtle.forward(distance)



sc.exitonclick()
