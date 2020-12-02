from graphics import  *
janela = GraphWin("Grid", 600, 600)

linha = Line(Point(0, 200), Point(599, 200))
linha.setFill("black")
linha.draw(janela)

linha2 = Line(Point(300, 0), Point(300, 599))
linha2.setFill("black")
linha2.draw(janela)

grid = GraphWin('Grid', 600, 600)

# Grid
for x in range(10):
    for y in range(10):
        grid.plotPixel(x*60, y*60, "black")

# Clique do mouse
    grid.getMouse()
    grid.close()
