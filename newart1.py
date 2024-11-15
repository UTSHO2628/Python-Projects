from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
penup()
goto(0, -100)  # Starting position
pendown()

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Get RGB color from HSV
        color(c)
        h += 0.005
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
    circle(40, 24)
done()
sss