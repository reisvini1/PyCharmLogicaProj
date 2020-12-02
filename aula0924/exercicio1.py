from graphics import  *
janela = GraphWin("Linhas", 600, 600)
# Diagonal Principal
dp = Line(Point(0, 0), Point(599, 599))
dp.setFill("red")
dp.draw(janela)

# Diagonal Secundária
ds = Line(Point(599, 0), Point(0, 599))
ds.setFill("orange")
ds.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
