from graphics import *

janela = GraphWin("Exercicios 3 Quadrados", 600, 600)

# Desenhando Quadrados

# Quadrado 1
quadrado1 = Rectangle(Point(99, 274), Point(149, 324))
quadrado1.setFill("green")
quadrado1.draw(janela)

# Quadrado 2
quadrado2 = Rectangle(Point(274, 274), Point(324, 324))
quadrado2.setFill("yellow")
quadrado2.draw(janela)

# Quadrado3
quadrado3 = Rectangle(Point(449, 274), Point(499, 324))
quadrado3.setFill("blue")
quadrado3.draw(janela)

# Clique Mouse
janela.getMouse()
janela.close()
