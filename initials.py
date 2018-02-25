import turtle

def initials():
    window = turtle.Screen()
    window.bgcolor("purple")
    Man = turtle.Turtle()
    Man.shape("turtle")
    Man.color("green")
    Man.speed(0.1)
    
    Man.left(60)
    Man.forward(100)
    Man.right(120)
    Man.forward(100)
    Man.backward(50)
    Man.left(60)
    Man.backward(50)

    Man.penup()
    Man.goto(150,100)
    Man.pendown()

    Man.right(90)
    Man.forward(100)
    Man.left(90)
    Man.forward(80)

    
    window.exitonclick()

initials()
    
