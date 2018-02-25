import turtle
x = 100
y= 90
def draw_square(random, x ,y):
    
    for i in range(1,5):
        random.forward(x)
        random.right(y)
        
def draw_shapes():

            
    window = turtle.Screen()
    window.bgcolor("yellow")
    jas = turtle.Turtle()
    jas.shape("turtle")
    jas.color("purple")
    jas.speed(20)
    aas = turtle.Turtle()
    aas.shape("turtle")
    aas.color("blue")
    aas.speed(20)
    bas = turtle.Turtle()
    bas.shape("arrow")
    bas.color("red")
    bas.speed(20)
    for i in range(1,37):
        draw_square(jas, 50,90)
        jas.right(10)
    for i in range(1,74):
        draw_square(aas, 100,90)
        aas.right(5)
    for i in range(1,148):
        draw_square(bas, 200,90)
        bas.right(2.5)
   

    window.exitonclick()
            
draw_shapes()



