#pong by Faris5242

import turtle


kek = turtle.Screen()
kek.title("Pong")
kek.bgcolor("black")
kek.setup(width=800, height=600)
kek.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") 
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#paddle c
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.penup()
paddle_c.goto(0, 0)
paddle_c.dx = 0.4
paddle_c.dy = 0.4

# Pen SD
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))




# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y +=40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=40
    paddle_b.sety(y)


#keyboard binding
kek.listen()
kek.onkeypress(paddle_a_up, "w" )
kek.onkeypress(paddle_a_down, "s")
kek.onkeypress(paddle_b_up, "Up")
kek.onkeypress(paddle_b_down, "Down")


# Main game loop 
while True:
    kek.update()


 #move the ball
    paddle_c.setx(paddle_c.xcor() + paddle_c.dx)
    paddle_c.sety(paddle_c.ycor()+paddle_c.dy)

 # Border checking

     # Top and bottom
    if paddle_c.ycor() > 290:
        paddle_c.sety(290)
        paddle_c.dy *= -1
       
    
    elif paddle_c.ycor() < -290:
        paddle_c.sety(-290)
        paddle_c.dy *= -1
      


        
# Left and right
    if paddle_c.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        Delay1=(paddle_c.goto(0, 0))
        paddle_c.dx *= -1
        
        

    elif paddle_c.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        paddle_c.goto(0, 0)
        paddle_c.dx *= -1






         # Paddle and ball collisions
    if paddle_c.xcor() < -340 and paddle_c.ycor() < paddle_a.ycor() + 50 and paddle_c.ycor() > paddle_a.ycor() - 50:
        paddle_c.dx *= -1 
        
    elif paddle_c.xcor() > 340 and paddle_c.ycor() < paddle_b.ycor() + 50 and paddle_c.ycor() > paddle_b.ycor() - 50:
        paddle_c.dx *= -1
      
