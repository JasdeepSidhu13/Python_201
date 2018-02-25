import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    def draw_square():
        
    
        jas = turtle.Turtle()
        jas.shape("turtle")
        jas.color("blue")
    
        i = 0
        while i < 4:
            jas.forward(100)
            jas.right(90)
            i=i+1 
    draw_square()

    def draw_circle():
        Net = turtle.Turtle()
        Net.shape("arrow")
        Net.color ("green")
        
        Net.circle(100)
    
        window.exitonclick()
    
    draw_circle()

    

draw_shapes()


