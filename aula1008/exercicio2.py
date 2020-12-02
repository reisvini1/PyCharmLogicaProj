from graphics import *
import math

# Janela
jan = GraphWin("Coração...", 600, 400)

tam = 100
passo = 0.001

# Equação cor.
x = -1
while x <= 1:
    y = -(-math.sqrt(1 - x ** 2) + math.sqrt(abs(x)))
    print(x,y)
    col = x * tam
    lin = y * tam
    jan.plot(col +300, lin + 200, "red")

    y = -(math.sqrt(1 - x ** 2) + math.sqrt(abs(x)))
    col = x * tam
    lin = y * tam
    jan.plot(col + 300, lin + 200, "red")

    x += passo

# Mouse
jan.getMouse()
jan.close()