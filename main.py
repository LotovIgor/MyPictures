import turtle

def sq(a, x, y):
  goto(x, y)
  turtle.pendown()        
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(a)
  turtle.left(90)
  turtle.penup()  

def rec(a, b, x, y):
  goto(x, y)
  turtle.pendown() 
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(b)
  turtle.left(90)
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(b)
  turtle.left(90)
  turtle.penup()  
  
def tri(size, flip):
    turtle.pendown()
    turtle.fill(True)
    for _ in range(3):
        if flip:
           turtle.left(120)
        turtle.forward(size)
        if not flip:
           turtle.right(120)
    turtle.penup()
