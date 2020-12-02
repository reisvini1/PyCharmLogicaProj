from graphics import *
import random

# Janela
janela = GraphWin("Polígono Aleatórios", 600, 600)

# Polígono
getkey = True
while getkey:
    key = janela.getKey()
    if key == "Escape":
        getkey = False

    else:
        pontos = []
        numPontos = random.randrange(3, 10)
        for num in range(numPontos):
            p = Point(random.randrange(0, 600), random.randrange(0, 600))
            pontos.append(p)
        key = janela.getKey()
        poli = Polygon(pontos)
        poli.setOutline(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        poli.setFill(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        poli.draw(janela)