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
  
