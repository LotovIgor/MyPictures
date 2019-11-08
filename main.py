import turtle
import math
from turtle import *
# !!!!!!!!После написания процедуры поворачиваем черепашку так, чтобы смотрела вправо, как в начале!!!!!


def square(x, y, size, color, angle):
    # Маша пишет функцию, рисующую квадрат
    # Поворот против часовой стрелки
    # Координаты левого нижнего угла квадрата
    # Пример:square(0, 0, 80, 'red', angle)
    turtle.goto(x, y)
    turtle.left(angle)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.left(angle)
    for _ in range(4):
      turtle.forward(size)
      turtle.left(90)
    turtle.right(45)
    turtle.backward(size/2)
    turtle.fillcolor(color)
    turtle.forward(size/2)
    turtle.right(135)
    turtle.penup()
    pass


def triangle(x, y, a, b, color, angle):
    # Игорь пишет функцию, рисующую треугольник
    # Треугольники только прямоугольные, вводим координаты острого угла при а
    # Пример: triangle(0, 0, 200, 100, 'red', 120)
    turtle.color(color)
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.up()
    pass


def rhomb(x, y, size, color, angle):
    # Нил пишет функцию, рисующую ромб
    pass


# Далее под комментариями пишем каждый свою часть кода, рисующую у каждого свой рисунок
# Маша рисует медведя

# Маша рисует верблюда

# Игорь рисует черепаху

# Игорь рисует змею

# Нил рисует

# Нил рисует

# Строка выхода из окна рисования по клику
turtle.exitonclick()
