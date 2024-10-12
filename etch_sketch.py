from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def turn_left():
    new_heading=tim.heading()+50
    tim.setheading(new_heading)
    """tim.left(degree)
    both function can be used"""

def turn_right():
    new_heading=tim.heading()-50
    tim.setheading(new_heading)
    """tim.right(degree)
    both function can be used"""

def clear():
    tim.clear() #to clear all the drawings made by a particular turtle
    tim.penup()
    tim.home() #moves the turtle to the orig. position(middle of screen)
    tim.pendown()

    
screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear,key="c")

screen.exitonclick()