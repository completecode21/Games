#simple ping pong game perform in turtle
#by @completecode21


#import libraries
import turtle
import winsound
import asyncio

#make window
win = turtle.Screen()
win.title("Pong by CompleteCode")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)  #stop windowns from manual updatation


#score
score_a = 0
score_b = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0 )


#ball 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("blue")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.2 #delata/change x
ball1.dy = -0.2  #delata/change y

#ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("red")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.2 #delata/change x
ball2.dy = -0.2  #delata/change y

#ball 3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("white")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = 0.3  #delata/change x
ball3.dy = 0.3  #delata/change y

#ball 4
ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("yellow")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = -0.1 #delata/change x
ball4.dy =  0.3  #delata/change y

#list of balls
balls = [ball1,ball2,ball3,ball4]

#pen (score card)
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",24,"normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


 #paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)   

#keyboard commands 
win.listen() #listen for keyboard input
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"x")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
    win.update()

    for ball in balls:
        #move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking
        #up border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        #down border
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        #left border
        if ball.xcor() >390: 
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
            pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))


        #right border
        if ball.xcor() <-390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
            pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))




        #paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)



        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)



        #Bot Player
        bot_accuracy = 80 #if value increase accuracy decrease and if value decrease accuracy increases
        closest_ball = balls[0]
        for ball in balls:
            if ball.xcor() > closest_ball.xcor():
                closest_ball = ball
        if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > bot_accuracy: 
                paddle_b_up()

        elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > bot_accuracy:
                paddle_b_down()