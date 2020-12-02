from graphics import *
import random

janela = GraphWin("Exercícios círculos RGB", 600, 600)

# Desenhando círculos
for raio in range(3, 100, 3):
    circ = Circle(Point(299, 299), raio)
    vermelho = random.randrange(0, 256)
    azul = random.randrange(0, 256)
    verde = random.randrange(0, 256)
    circ.setOutline(color_rgb(vermelho, verde, azul))
    circ.draw(janela)

# Clique mouse
janela.getMouse()
janela.close()