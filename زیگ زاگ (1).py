from turtle import *
t=Turtle()
t.left(75)
for i in range(10):
    t.forward(150)
    if i%2==0:
        t.right(150)
    else:
        t.left(150)
    