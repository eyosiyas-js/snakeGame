# classic pong game
# created by Eyosiyas Tefera
# creater contact = eyosiyasat@gmail.com

# part 1
import turtle


win=turtle.Screen() # its makes to play the game in screen
win.title("pong by Eyosiyas Tefera ") # the name of the game
win.bgcolor("orange") #the color of the screen
win.setup(width=800,height=600) # the game width and hight
win.tracer(0) # its a ting that makes the game to run properly
# score
score_a=0
score_b=0

# paddle A # its a a box to kike the bole
paddle_a=turtle.Turtle() # the first ting you have to do when you creating a paddle
paddle_a.speed(0)
paddle_a.shape("square") # shape of the paddle
paddle_a.color("white") # the color of the paddle
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # its the length of width of the paddle
paddle_a.penup()
paddle_a.goto(-350,0) # its the place where the paddle stays

# paddle B   # its a a box to kike the bole
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball C
ball_c=turtle.Turtle()
ball_c.speed(0)
ball_c.shape("circle")
ball_c.color("white")
ball_c.penup()
ball_c.goto(0,0)
# 2 kinds of ball movement
ball_c.dx=0.5 # its a first movement
ball_c.dy=-0.5 # its a second movement
#pen aligh courier
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("player A:0  player B:0",align="center",font=("courier",24,"normal"))
# function
# up for paddle a
def paddle_a_up(): # its a def about the game to move
    y= paddle_a.ycor() # is makes the paddle to move up or down its name is ycor
    y += 20 #its a code to run the ycor and its has to be + b/c it moves to up
    paddle_a.sety(y) # its make the ycor in paddle a
# down for paddle b
def paddle_a_down():
    y= paddle_a.ycor() # is makes the paddle to move up or down its name is ycor
    y -= 20 # its a code to run the ycor and its has to be - b/c it moves to down
    paddle_a.sety(y) # its make the ycor in paddle a
def paddle_b_up(): # its a def about the game to move
    y= paddle_b.ycor() # is makes the paddle to move up or down its name is ycor
    y += 20 #its a code to run the ycor and its has to be + b/c it moves to up
    paddle_b.sety(y) # its make the ycor in paddle b
# down for paddle b
def paddle_b_down():
    y= paddle_b.ycor() # is makes the paddle to move up or down its name is ycor
    y -= 20# its a code to run the ycor and its has to be - b/c it moves to down
    paddle_b.sety(y) # its make the ycor in paddle b
# keybord usement
win.listen() # it makes the computer to listen and the game run by keybord
win.onkeypress(paddle_a_up,"w") # its makes "w" to move up the paddle a
win.onkeypress(paddle_a_down,"s") # its makes "s" to move down the paddle a
win.onkeypress(paddle_b_up,"o") # its makes "8" to move up the paddle b
win.onkeypress(paddle_b_down,"l") # its makes "2" to move down the paddle b
# part2
while True: # its makes the game to repeat when you score or somebody score in your goal
    win.update() # it makes the game to update in your pc or computer

    # move the ball
    ball_c.setx(ball_c.xcor()+ball_c.dx) # its a code to move the ball
    ball_c.sety(ball_c.ycor()+ball_c.dy) # its a code to move the ball

    # border
    if ball_c.ycor()> 290: # its a code to second one
        ball_c.sety(290) # its a code to stop in 290
        ball_c.dy *=-1 # its a code to bounce the ball b/c when we find the solution its give -2 its reverce to dy(2) so it make to bounce another direction
    if ball_c.ycor() < -290:  # its a code to second one
        ball_c.sety(-290)  # its a code to stop in -290
        ball_c.dy *= -1  # its a code to bounce the ball b/c when we find the solution its give -2 its reverce to dy(2) so it make to bounce another direction

    if ball_c.xcor() > 390:  # its a code to second one {}
        ball_c.goto(0,0)
        ball_c.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if ball_c.xcor() < -390:  # its a code to second one {} .
        ball_c.goto(0,0)
        ball_c.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    # ball and paddle collisions

    if ball_c.xcor() > 340 and ball_c.xcor() < 350 and  (ball_c.ycor()<paddle_b.ycor() + 40 and ball_c.ycor()>paddle_b.ycor() -40):
        ball_c.setx(340)
        ball_c.dx *= -1

    if ball_c.xcor() < -340 and ball_c.xcor() > -350 and  (ball_c.ycor()<paddle_a.ycor() + 40 and ball_c.ycor()>paddle_a.ycor() -40):
        ball_c.setx(-340)
        ball_c.dx *= -1