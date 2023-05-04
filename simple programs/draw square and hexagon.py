import turtle

trtl=turtle.Turtle()

for i in range(4):
  trtl.forward(25)
  trtl.right(90)
  
trtl.penup()
trtl.forward(100)
trtl.pendown()

for i in range(6):
  trtl.forward(25)
  trtl.right(60)
  
  turtle.done()
