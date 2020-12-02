from graphics import *

win = GraphWin("Bandeira do Brasil", 1000, 600)
win.setBackground("green")

def main():


   p = Polygon(Point(100, 300), Point(500, 550), Point(900, 300), Point(500, 50))
   p.setFill(color_rgb(254, 223, 0))
   p.setOutline(None)
   p.draw(win)

   circle = Circle(Point(500, 300), 150)
   circle.setFill("dark blue")
   circle.setOutline(None)
   circle.draw(win)

   for i in range(240, 260):
       x = - 0.5
       while x < 1.5:
           y = x ** 2
           win.plot(430 + (x * 145), i + (y * 30), "white")
           x += 0.005



main()

win.getMouse()
win.close()


