from graphics import *

def triangulo(pointse, pointid, win):

    pointse = Point(pointse.getX(), pointse.getY())
    pointid = Point(pointid.getX(), pointid.getY())

    ccol = int((pointid.getX() - pointse.getX()) / 2)

    col = pointse.getX()
    linha = pointid.getY()
    point1 = Point(col, linha)

    col = pointse.getX() + ccol
    linha = pointse.getY()
    point2 = Point(col, linha)

    p = Polygon(point1, point2, pointid)
    p.draw(win)

    win.getMouse()
    win.close()
