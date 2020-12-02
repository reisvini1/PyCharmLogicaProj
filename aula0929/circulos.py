from graphics import *

janela = GraphWin("Circulos", 600, 600)

# Desenhando Circulos
circulo = Circle(Point(299, 299), 50)
circulo.setOutline("black")
circulo.draw(janela)

circmenor = Circle(Point(299, 299), 30)
circmenor.setFill("purple")
circmenor.draw(janela)

# Clique mouse
janela.getMouse()
janela.close()