from turtle import *
import random
speed(0)
def square():
    for side in range(4):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        begin(fill)
        color(red,green,blue)
        forward(100)
        right(90)
        end(fill)

for layer in range(4):
    for i in range(4):
        square()
        forward(100)
    backward(400)
    left(90)
    forward(100)
    right(90)
