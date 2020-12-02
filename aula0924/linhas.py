from graphics import  *
janela = GraphWin("Linhas", 600, 400)

# Desenhando Linhas
linha = Line(Point(0, 200), Point(599, 200))
linha.setFill("green")
linha.draw(janela)

# Linha no meio
linha2 = Line(Point(300, 0), Point(300, 399))
linha2.setFill("blue")
linha2.draw(janela)

# Diagonal Principal
dp = Line(Point(0, 0), Point(599, 399))
dp.setFill("red")
dp.draw(janela)

# Diagonal Secundária
ds = Line(Point(599, 0), Point(0, 399))
ds.setFill("orange")
ds.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
