# create game "Pongi"

import turtle # a library for graphics

wn = turtle.Screen()
wn.title("First game learned: pongi")
wn.bgcolor("black")
wn.setup(width=800, height=500)
wn.tracer(0)

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1) # keep the len, expand width 5 times
paddleA.penup() # no drawing when moving
paddleA.goto(-350, 0)  

#paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#


#main game loop
while True:
    wn.update()