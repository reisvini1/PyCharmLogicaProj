from graphics import *
import random

janela = GraphWin("Pontos Aleatórios", 600, 400)

for i in range(30000):
    coluna = random.randrange(0, 600)
    linha = random.randrange(0, 600)
    ponto = Point(coluna, linha)
    ponto.setFill("Blue")
    ponto.draw(janela)

# Clique do mouse
janela.Getmouse()
janela.close()