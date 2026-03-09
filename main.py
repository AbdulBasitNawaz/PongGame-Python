import turtle
import pygame

wn = turtle.Screen()
wn.title("Pong by TokyoEDTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
clock = pygame.time.Clock() # For controlling FPS

# Score Box
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()

score_a = 0
score_b = 0
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal") )

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Fucntion
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Key Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    # FPS control
    clock.tick(90)

    # Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()  + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal") )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal") )

    # Check Paddle and Ball Collision
    if (ball.xcor() >  340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <  -340 and ball.xcor() > -350) and (ball.ycor() > paddle_a.ycor() - 40) and (ball.ycor() < paddle_a.ycor() +40):
        ball.setx(-340)
        ball.dx *= -1

    # Check Paddle and wall collision
    if paddle_a.ycor() > 240:
        paddle_a.sety(240)

    if paddle_a.ycor() < -238:
        paddle_a.sety(-238)

    if paddle_b.ycor() > 240:
        paddle_b.sety(240)

    if paddle_b.ycor() < -238:
        paddle_b.sety(-238)