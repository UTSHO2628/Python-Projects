from turtle import *
import time

# ফাংশন যা হৃদয় আঁকে
def draw_heart():
    color("red")
    begin_fill()
    pensize(10)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

# ফাংশন যা বিভিন্ন রঙের বৃত্ত আঁকে
def draw_circle(radius, color_name):
    penup()
    goto(0, -radius)
    pendown()
    color(color_name)
    circle(radius)

# ফাংশন যা স্ক্রীনে বিভিন্ন রঙের সরল রেখা আঁকে
def draw_lines():
    colors = ["blue", "green", "purple", "orange", "black"]
    for i in range(5):
        penup()
        goto(-200, i * 50)
        pendown()
        color(colors[i])
        forward(400)

# স্ক্রীন সেটআপ
bgcolor("white")
speed(3)

# হৃদয় আঁকো
draw_heart()

# এক সেকেন্ড অপেক্ষা
time.sleep(1)

# পাঁচটি বৃত্ত আঁকো বিভিন্ন রঙে
radius = 50
for i in range(5):
    draw_circle(radius + i * 30, ["yellow", "blue", "green", "purple", "orange"][i])

# এক সেকেন্ড অপেক্ষা
time.sleep(1)

# স্ক্রীনের বিভিন্ন লাইনে বিভিন্ন রঙে আঁকো
draw_lines()

# এক সেকেন্ড অপেক্ষা
time.sleep(1)

# স্ক্রীনটি বন্ধ না হওয়া পর্যন্ত খুলে রাখো
done()
