from graphics import *
def main():
    grid = GraphWin('Grid', 600, 600)

# Fazendo o grid
    for x in range(10):
        for y in range(10):
            grid.plotPixel(x*60, y*60, "black")

# Clique do mouse
    grid.getMouse()
    grid.close()

main()
