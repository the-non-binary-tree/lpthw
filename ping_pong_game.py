import turtle


sr=turtle.Screen()
sr.title('ping_pong_game')
sr.colormode(255)
sr.bgcolor(50,100,50)
sr.setup(width=800, height=500)
sr.tracer(8)

#Game objects
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color(105,0,0)
ball.penup()
ball.setpos(0,0)
ball.dx=1
ball.dy=-1

#paddle_a
pa=turtle.Turtle()
pa.speed(0)
pa.shape('square')
pa.color('black')
pa.shapesize(5,1)
pa.penup()
pa.setpos(-370,0)

#paddle_b
pb=turtle.Turtle()
pb.speed(0)
pb.shape('square')
pb.color('black')
pb.shapesize(5, 1)
pb.penup()
pb.setpos(370,0)

#move paddle a 
#move paddle a up
def pa_up():
    y=pa.ycor()
    y+=15
    pa.sety(y)

#move paddle a down
def pa_down():
    y=pa.ycor()
    y-=15
    pa.sety(y)

#move paddle b up
def pb_up():
    y=pb.ycor()
    y+=15
    pb.sety(y)

#move paddle b down
def pb_down():
    y=pb.ycor()
    y-=15
    pb.sety(y)

#keyboard binding
sr.listen()
sr.onkey(pa_up,'w')
sr.onkey(pa_down,'s')
sr.onkey(pb_up,'i')
sr.onkey(pb_down,'k')

#score
score=turtle.Turtle()
score.speed(0)
score.color(255,123,20)
score.penup()
score.hideturtle()
score.goto(0,210)
score.write('Paddle a: 0 Paddle b: 0', align='center',font=('calibri',25,'bold'),)
score_a=0
score_b=0

#GAME LOOP
while True:
    sr.update()
    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking upper border
    if ball.ycor()>235:
        ball.sety(235)
        ball.dy*=-1
    
    #border checking lower border
    if ball.ycor()<-235:
        ball.sety(-235)
        ball.dy*=-1

    #border checking left border
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        ball.setpos(0,0)
        score_b +=1
        score.clear()
        score.write('Paddle a: 0 Paddle b: 0', align='center',font=('calibri',25,'bold'),)

    #border checking right border
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        ball.setpos(0,0)
        score_b +=1
        score.clear()
        score.write('Paddle a: 0 Paddle b: 0', align='center',font=('calibri',25,'bold'),)

    #ball imteracting with paddle b
    if (ball.xcor()>350 and ball.xcor()<370) and (ball.ycor()<(pb.ycor() + 50) and ball/ycor()>(pa.ycor() -50)):
        ball.setx(-330)
        ball.dx*=-1
        



