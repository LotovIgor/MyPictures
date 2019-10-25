import turtle

def square(x, y, size, color):
    # Маша пишет функцию, рисующую квадрат
    turtle.goto(x, y)
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

def triangle(x, y, size, color, angle):
    # Игорь пишет функцию, рисующую треугольник
    pass

def rhomb(x, y, size, color, angle):
    # Нил пишет функцию, рисующую ромб
    pass