#Python program to use the Turtle library to draw a Tic-Tac-Toe Board

#Get Turtle library and set as t
import turtle as t

#configure Turtle to draw thick red lines
t.pensize(10)
t.color('red')

#Lift the pen and move to top of the left vertical line
t.penup()
t.goto(-100,200)

#put pen down, point south, and move to bottom of tic-tac-toe grid
t.pendown()
t.setheading(270)
t.forward(400)