from graphics import *
import random

janela = GraphWin("Poligonos", 600, 600)

ficar = True
while ficar:
    tecla = janela.getKey()
    print(tecla)
    if tecla == 'Escape':
        ficar = False
    else:
        pontos = []
        numpontos = random.randrange(3, 10)
        for num in range(numpontos):
            p = Point(random.randrange(0, 600), random.randrange(0, 600))
            pontos.append(p)

            pol = Polygon(pontos)
            pol.setOutline(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            pol.setFill(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            pol.draw(janela)
# Desenhando círculo



    janela.getMouse()
    janela.close()