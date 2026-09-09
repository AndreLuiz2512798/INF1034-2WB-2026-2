from turtle import *
from time import sleep

t = Turtle()

def retangulo(x, y, base, altura, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(0, 2):
        t.forward(base)
        t.left(90)
        t.fd(altura)
        t.lt(90)
    t.end_fill()

def circulo(x, y, raio, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def estrela(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(0, 5):
        t.forward(lado)
        t.right(144)
        t.fd(lado)
        t.left(72)
    t.end_fill()

def desenha_franca():
    retangulo(-200, 200, 50, 100, "#012654")
    retangulo(-150, 200, 50, 100, "#FFFFFF")
    retangulo(-100, 200, 50, 100, "#CE1126")

def desenha_italia():
    retangulo(-200, 200, 50, 100, "#009246")
    retangulo(-150, 200, 50, 100, "#FFFFFF")
    retangulo(-100, 200, 50, 100, "#CE2B37")

def desenha_costa_rica():
    retangulo(0, 0, 300, 200, "#001489")
    retangulo(0, 50, 300, 100, "#FFFFFF")
    retangulo(0, 75, 300, 50, "#DA291C")
    circulo(80, 85, 15, "#FFFFFF")

def desenha_noruega():
    retangulo(0, 0, 200, 150, "#BA0B2F")
    retangulo(50, 0, 50, 150, "#FFFFFF")
    retangulo(0, 60, 200, 50, "#FFFFFF")
    retangulo(0, 75, 200, 22, "#00205B")
    retangulo(65, 0, 22, 150, "#00205B")
    
def desenha_finlandia():
    retangulo(0, 0, 200, 150, "#FFFFFF")
    retangulo(50, 0, 50, 150, "#002F6C")
    retangulo(0, 60, 200, 50, "#002F6C")

def desenha_islandia():
    retangulo(0, 0, 200, 150, "#03529C")
    retangulo(50, 0, 50, 150, "#FFFFFF")
    retangulo(0, 60, 200, 50, "#FFFFFF")
    retangulo(0, 75, 200, 22, "#DC1F36")
    retangulo(65, 0, 22, 150, "#DC1F36")

def desenha_emirados_arabes():
    retangulo(0, 0, 50, 99, "#C8112E")
    retangulo(50, 0, 100, 33, "#000000")
    retangulo(50, 33, 100, 33, "#FFFFFF")
    retangulo(50, 66, 100, 33, "#01843E")

def desenha_guine_bissau():
    retangulo(0, 0, 50, 100, "#CE1126")
    retangulo(50, 0, 100, 50, "#009E49")
    retangulo(50, 50, 100, 50, "#FCD215")
    estrela(30, 50, 10, "black")

def desenha_japao():
    retangulo(0, 0, 200, 100, "#FFFFFF")
    circulo(100, 25, 25, "#BC002D")

def desenha_honduras():
    retangulo(0, 0, 200, 99, "#0D3B99")
    retangulo(0, 33, 200, 33, "#FFFFFF")
    estrela(100, 49, 5, "#0D3B99")
    estrela(70, 59, 5, "#0D3B99")
    estrela(130, 59, 5, "#0D3B99")
    estrela(70, 42, 5, "#0D3B99")
    estrela(130, 42, 5, "#0D3B99")

def desenha_georgia():
    retangulo(0, 0, 200, 150, "#FFFFFF")
    retangulo(0, 62.5, 200, 25, "#FF0000")
    retangulo(87.5, 0, 25, 150, "#FF0000")
    retangulo(20, 115, 40, 10, "#FF0000")
    retangulo(35, 100, 10, 40, "#FF0000")
    retangulo(140, 115, 40, 10, "#FF0000")
    retangulo(155, 100, 10, 40, "#FF0000")
    retangulo(20, 25, 40, 10, "#FF0000")
    retangulo(35, 10, 10, 40, "#FF0000")
    retangulo(140, 25, 40, 10, "#FF0000")
    retangulo(155, 10, 10, 40, "#FF0000")

def desenha_forma_nepal(x, y, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    t.goto(x, y + 300)
    t.goto(x + 220, y + 170)
    t.goto(x + 80, y + 170)
    t.goto(x + 250, y)
    t.goto(x, y)
    t.end_fill()

def desenha_lua_nepal(x, y, cor1, cor2):
    t.pu()
    t.goto(x, y)
    t.pd()
    circulo(35, cor1)
    t.pu()
    t.goto(x, y + 15)
    t.pd()
    circulo(35, cor2)

def desenha_estrela_nepal(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for count in range(0, 12):
        t.forward(lado)
        t.right(150)
        t.forward(lado)
        t.left(120)
    t.end_fill()

def desenha_nepal():
    desenha_forma_nepal(0, 0, "#DC143C")
    desenha_lua_nepal(70, 170, "white", "#DC143C")
    desenha_estrela_nepal(75, 200, 10, "white")
    desenha_estrela_nepal(70, 70, 25, "white")

# desenha_franca()

# sleep(1)
# t.clear()

# desenha_italia()

# sleep(1)
# t.clear()

# desenha_costa_rica()

# sleep(1)
# t.clear()

# desenha_noruega()

# sleep(1)
# t.clear()

# desenha_finlandia()

# sleep(1)
# t.clear()

# desenha_islandia()

# sleep(1)
# t.clear()

# desenha_emirados_arabes()

# sleep(1)
# t.clear()

# desenha_guine_bissau()

# sleep(1)
# t.clear()

# desenha_japao()

# sleep(1)
# t.clear()

# desenha_honduras()

# sleep(1)
# t.clear()

desenha_georgia()

sleep(1)
t.clear()

desenha_nepal()

sleep(1)
t.clear()



mainloop()