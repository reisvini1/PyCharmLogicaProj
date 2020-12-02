from graphics import *

janela = GraphWin("Exercício círculos e retângulos", 600, 600)
x = 15

# Desenhando círculo
for raio in range(0, 19):
    circ = Circle(Point(300, 300), x)
    circ.setOutline("purple")
    circ.draw(janela)

# Desenhando retângulos
    retangulo = Rectangle(Point(300 - x, 300 - x), Point(300 + x, 300 + x))
    retangulo.setOutline("black")
    retangulo.draw(janela)
    x+= 15
# Clique do mouse
janela.getMouse()
janela.close()