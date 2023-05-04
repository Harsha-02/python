import turtle

trtl=turtle.Turtle()

for i in range(4):
  trtl.forward(25)
  trtl.left(90)
  
trtl.penup()
trtl.backward(100)
trtl.pendown()

for i in range(6):
  trtl.forward(25)
  trtl.left(60)
  
trtl.penup()
trtl.forward(200)
trtl.pendown()

trtl.circle(25)
  
turtle.done()
  
