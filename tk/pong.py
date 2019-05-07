import turtle

wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.delay(0)

#paddle_l
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("black")
paddle_l.resizemode("user")
paddle_l.shapesize(5, 1)
paddle_l.penup()
paddle_l.goto(-380,0)
paddle_l.color("white")
#paddle_r
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("black")
paddle_r.resizemode("user")
paddle_r.shapesize(5, 1)
paddle_r.penup()
paddle_r.goto(370,0)
paddle_r.color("white")
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.color("white")
ball.dx=3
ball.dy=-3
#functions - moving paddles
def paddle_l_up():
    y=paddle_l.ycor()
    y+=20
    paddle_l.sety(y)
def paddle_l_down():
    y=paddle_l.ycor()
    y-=20
    paddle_l.sety(y)
def paddle_r_up():
    y=paddle_r.ycor()
    y+=20
    paddle_r.sety(y)
def paddle_r_down():
    y=paddle_r.ycor()
    y-=20
    paddle_r.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")


while True:
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy*-1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy = ball.dy*-1
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
    #collision paddle and ball
    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() -40):
        ball.setx(-350)
        ball.dx *= -1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() -40):
        ball.setx(350)
        ball.dx *= -1

    

wn.mainloop()   