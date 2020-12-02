
from graphics import *

janela = GraphWin("Pontos ...", 600, 400)

# Desenhando pontos método-1 (quatro pixels)
ponto = Point(100, 100)
ponto.setFill("Blue")
ponto.draw(janela)

# Desenhando pontos método-2 (um pixel)
janela.plot(200,200,"black")

#(Meio Coluna)
for coluna in range(0, 600, 4):
    p = Point(coluna, 300)
    p.setFill("Red")
    p.draw(janela)
    time.sleep(0.02)

#(Meio Linha)
for linha in range(0, 600, 4):
    p = Point(300, linha)
    p.setFill("Red")
    p.draw(janela)
    time.sleep(0.02)

#(Diagonal)
for pos in range(0, 600, 4):
    p = Point(pos, pos)
    p.setFill("Red")
    p.draw(janela)
    time.sleep(0.02)

#(Outra Diagonal)
    p = Point(599 - pos, pos)
    p.setFill("Red")
    p.draw(janela)
    time.sleep(0.02)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
