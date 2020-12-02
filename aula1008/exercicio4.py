from graphics import *
import time
janela = GraphWin("Grid", 400, 400)

color = "red"

for col in range(0, 400, 5):
    if color == "red":
        color = "blue"
    else:
        color = "red"

    for lin in range(0, 400, 5):
        if color == "red":
            color = "blue"
        else:
            color = "red"

        retangulo = Rectangle(Point(col, lin), Point(col + 5, lin + 5))
        retangulo.setFill(color)
        retangulo.draw(janela)
        time.sleep(.0)

# Clique do mouse
janela.getMouse()
janela.close()