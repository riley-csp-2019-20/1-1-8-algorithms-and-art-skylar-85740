#New Clown design for masks

import turtle as trtl 
clown = trtl.Turtle()
#creating the pentagon first
t = trtl.Turtle()
clown.pensize(3)
clown_count = 0
while (clown_count < 5):
    clown_x = t.xcor()
    clown_y = t.ycor()
    clown.forward(200)
    clown.left(72)
    clown_count += 1
    clown.fillcolor("red")
#pentagon complete
#now starting the stars




















wn = trtl.Screen()
wn.mainloop()
