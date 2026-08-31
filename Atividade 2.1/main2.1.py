from turtle import *

t = Turtle()
# t.shape("turtle")

t.pu()
t.goto(-400, 0)
t.pd()
t.goto(400,0)
t.stamp()
t.pu()
t.goto(0, -400)
t.left(90)
t.pd()
t.goto(0, 400)
t.stamp()
t.pu()
t.right(90)

t.goto(100, 100)
t.pd()
t.color("black")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for count in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.pu()
t.goto(-300, 100)
t.pd()

var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for count in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

t.pu()
t.goto(-300, -300)
t.pd()

var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for count in range(5):
    t.forward(100)
    t.left(72)
t.end_fill()

t.pu()
t.goto(100, -300)
t.pd()

var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for count in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()

t.pu()
t.goto(300, 100)
t.pd()

for count in range(30):
    t.forward(count)
    t.left(50)
    
t.end_fill()

mainloop()