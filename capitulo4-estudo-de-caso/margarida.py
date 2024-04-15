import turtle


t = turtle.Turtle()
t.speed(0)  
t.width(3)  


turtle.bgcolor("green")


def petala():
    t.color("white")  
    t.begin_fill()  
    t.circle(60, 70)  
    t.left(120)  
    t.circle(60, 70)  
    t.end_fill() 


def centro():
    t.penup()
    t.goto(-5, -35) 
    t.color("yellow")  
    t.begin_fill()  
    t.circle(20)  
    t.end_fill()  


for _ in range(17):
    petala()
    t.left(36)


centro()

t.penup()
t.forward(200)


turtle.done()
