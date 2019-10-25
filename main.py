import turtle

def square(x, y, size, color):
    # Пишет функцию, рисующую квадрат
    goto(x, y)
    turtle.pendown()        
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.penup()  
    pass

def triangle(x, y, size, color, angle, type):
    # Пишет функцию, рисующую треугольник
    pass

def rhomb(x, y, size, color, angle):
    # Пишет функцию, рисующую ромб
    pass
