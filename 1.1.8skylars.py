#New Clown design for masks

import turtle as trtl 
clown = trtl.Turtle()
#creating the pentagon first
t = trtl.Turtle()
clown.pensize(3)
side_count = 0
while (side_count < 5):
    clown_x = t.xcor()
    clown_y = t.ycor()
    clown.forward(200)
    clown.left(72)
    clown_count += 1
    clown.fillcolor("red")
#pentagon complete
#now starting the stars
star_count = 0
while (star_count < 2):
    if (star_count < 1):
        point_count = 0
        while (point_count < 0):
            clown.penup()
            clown.goto()
            clown.pendown()
            clown.forward()
            clown.right()
            clown.forward()
            clown.left()
            clown_count += 1
            clown.fillcolor()
    else (star_count < 2):
        point count = 1
        while (point_count < 6):
            clown.penup()
            clown.goto()
            clown.pendown()
            clown.




















wn = trtl.Screen()
wn.mainloop()
