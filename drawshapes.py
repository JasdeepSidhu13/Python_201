1import turtle

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
    
    for i in range(1,4):   
        draw_square()
        brad = turtle.Turtle()
        brad.right(10)
    

    def draw_circle():
        Net = turtle.Turtle()
        Net.shape("arrow")
        Net.color ("green")
        
        Net.circle(100)
    
        
    
    draw_circle()

    def draw_triangle():
        virat = turtle.Turtle()
        virat.shape("square")
        virat.color("red")

        object = [1, 2 ,3]
        
        i=0
        while i < 3:
            virat.forward(100)
            virat.right(120)
            i = i + 1
            '''
        for i in object :
            virat.forward(200)
            virat.right(120)
            i = i + 1
        for i in range(1,4) :
            virat.forward(400)
            virat.right(120)
            '''
            
        window.exitonclick()
        
    draw_triangle()
        
        

    

draw_shapes()


