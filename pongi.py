# create game "Pongi"

import turtle # a library for graphics

wn = turtle.Screen()
wn.title("pongi")
wn.bgcolor("black")
wn.setup(width=800, height=500)
wn.tracer(0)

#score
score_a = 0
score_b = 0

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
ball.speed(0) # i cant slow down the speed of the ball though i change the speed parameters :<
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1 # it means that the ball will 
ball.dy = 1 # moves 1 pixels in each dimension x and y
 
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Player A: 0, Player B: 0", align='center', font={'Courier', 24, 'normal'})


#function
def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)
def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)
def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


 

#main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 240: #checking on the up border
        ball.sety(240)
        ball.dy *= -1
    
    if ball.ycor() < -240: #checking on the bottom border
        ball.sety(-240)
        ball.dy *= -1
    
    if ball.xcor() > 390: #checking on the right
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align='center', font={'Courier', 24, 'normal'})
    
    if ball.xcor() < -390: #checking on the left
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align='center', font={'Courier', 24, 'normal'})
    
    # the collisions between 2 paddle with the ball
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1