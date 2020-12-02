from graphics import *

janela = GraphWin("Retângulos", 600, 600)
# Desenhando retângulos
retangulo = Rectangle(Point(10,10), Point(599, 100))
retangulo.setFill("blue")
retangulo.setOutline("black")
retangulo.draw(janela)

# Clique do mouse
janela.getMouse()
janela.close()