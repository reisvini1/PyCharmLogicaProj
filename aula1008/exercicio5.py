from graphics import *

janela = GraphWin("Túnel de quadrados", 400, 400)

# Túnel de mentira
for posicao in range(50, 325, 3):
   ret = Rectangle(Point(posicao, posicao), Point(posicao + 40, posicao + 40))
   ret.setOutline(color_rgb(0, 50, 255))
   ret.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
