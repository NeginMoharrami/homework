from turtle import *
t=Turtle()
a=0
while a<360:
    for i in range(4):
      t.forward(50)
      t.right(90)
    t.left(10)
    a+=10