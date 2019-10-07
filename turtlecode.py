from turtle import *

penup()
goto(-200,-200)
pendown()

def square():
    for j in range(4):
        for i in range(4):
            forward(100)
            right(90)
        forward(100)

    

for x in range(4):
    penup()
    goto(-200,100*x)
    pendown()
    square()
