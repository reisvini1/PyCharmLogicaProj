from graphics import *
import random

janela = GraphWin("Exercício getkey", 600, 600)

flag = True
while flag:
    tecla = janela.getKey()
    if tecla == "Escape":
        flag = False
    else:
        col = random.randrange(10, 590)
        lin = random.randrange(10, 590)
        x = random.randrange(5, 30)
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)

        if tecla == 'C' or tecla == 'c':
            circ = Circle(Point(col, lin), x)
            circ.setOutline(color_rgb(r, g, b))
            circ.draw(janela)
        if tecla == 'R' or tecla == 'r':
            ret = Rectangle(Point(col - x, lin - x), Point(col + x, lin + x))
            ret.setOutline(color_rgb(r, g, b))
            ret.draw(janela)

# Clique do mouse
janela.getMouse()
janela.close()