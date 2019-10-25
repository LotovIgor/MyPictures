import turtle

def square(x, y, size, color, angle):
    # Маша пишет функцию, рисующую квадрат
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(angle)
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

def triangle(x, y, a, b, color, angle):
    # Игорь пишет функцию, рисующую треугольник
    pass

def rhomb(x, y, size, color, angle):
    # Нил пишет функцию, рисующую ромб
    pass

# Далее под комментариями пишем каждый свою часть кода, рисующую у каждого свой рисунок
# Маша рисует медведя

# Маша рисует верблюда

# Игорь рисует

# Игорь рисует

# Нил рисует

# Нил рисует
