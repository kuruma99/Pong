# Simple Pong in Python3 for beginners
# Author : Mridul Singh

import turtle 
import os

wn = turtle.Screen() # created a window using turle for the game
wn.title("Pong by kuruma") # adds title
wn.bgcolor("black") # sets black as the background color
wn.setup(width=800, height=600) # configuring the size of the game window
wn.tracer(0)

# Score
score_a = 0 # score of player A
score_b = 0 # score of player B

# Paddle A
paddle_a = turtle.Turtle() # paddle_a is an instance of class Turtle of turtle module
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretches the width 5 times 
paddle_a.penup() # to not draw a line while moving
paddle_a.goto(-350, 0) # initial coordinates of the paddle

# Paddle B
paddle_b = turtle.Turtle() # paddle_b is an instance of class Turtle of turtle module
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretches the width 5 times 
paddle_b.penup() # to not draw a line while moving
paddle_b.goto(350, 0) # initial coordinates of the paddle

# Ball
ball = turtle.Turtle() # ball is an instance of class Turtle of turtle module
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() # to not draw a line while moving
ball.goto(0, 0) # initial coordinates of the paddle
ball.dx = 0.05
ball.dy = 0.05

# Pen 
pen = turtle.Turtle() # a Turltle instance for score keeping
pen.speed(0) # animation speed not moving speed
pen.color("white")
pen.penup() # to not draw a line while moving
pen.hideturtle() # to hide the turtle
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): # To move paddle up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main game loop
while True:
    wn.update() # everytime the loop executes it updates the game window

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1;
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1;
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font =("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav")

         

