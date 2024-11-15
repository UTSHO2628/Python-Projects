from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
penup()
goto(0, -100)  # Adjusted starting position for smaller heart
pendown()

# Function to draw a smaller heart shape
def draw_heart():
    begin_fill()
    left(50)
    forward(150)  # Reduced size of forward movement
    circle(75, 200)  # Reduced circle radius for a smaller heart curve
    right(140)
    circle(75, 200)  # Reduced circle radius for symmetry
    forward(150)  # Reduced size of forward movement
    end_fill()

# Change pen color and fill color dynamically based on HSV
for i in range(36):
    c = colorsys.hsv_to_rgb(h, 1, 1)  # Get RGB color from HSV
    color(c)  # Set the dynamic color
    h += 0.03  # Increment hue
    draw_heart()  # Draw heart shape
    right(10)  # Rotate for next heart

done()
