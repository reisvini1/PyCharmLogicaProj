from graphics import *
import random

win = GraphWin("Bolinha ...", 800, 600)
win.setBackground("Black")

linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(10)
linhaSuperior.setFill("white")
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setFill("white")
linhaInferior.draw(win)

col = 390
lin = 80
raio = 15
circulo = Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(255, 0, 127))
circulo.draw(win)

colIni = 340
tamanho = 100
barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
barra.setFill(color_rgb(57, 255, 20))
barra.setWidth(10)
barra.draw(win)

pts = 0
pontos = Text(Point(400, 575), "Pontos: " + str(pts))
pontos.setSize(14)
pontos.setFill("white")
pontos.draw(win)

# Chances
chan = 3
chances = Text(Point(100, 575), "Chances = " + str(chan))
chances.setSize(14)
chances.setFill("white")
chances.draw(win)

velocidade = 5
bateu = True
continuar = True
while continuar:

    if bateu:
        passo = random.randrange(1, 10)
        if random.random() < 0.5:
            passo = -passo
        bateu = False

    if (col + raio + passo) > 800:
        passo = -passo

    if (col - raio + passo) < 0:
        passo = -passo

    if lin < 65:
        velocidade = -velocidade

    if lin == 515 and col > colIni and col < (colIni + tamanho):
        velocidade = -velocidade


    # Nova posição do círculo
    circulo.undraw()
    col += passo
    lin += velocidade
    circulo = Circle(Point(col, lin), 15)
    circulo.setFill(color_rgb(255, 0, 127))
    circulo.draw(win)

    # Movimento horizontal da barra pelas setas direita/esquerda
    tecla = win.checkKey()

    # Sair do joguinho
    if tecla == "Escape":
        continuar = False
        continue

    if tecla == "Right":
        if (colIni + 20) < 701:
            colIni = colIni + 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setFill(color_rgb(57, 255, 20))
        barra.setWidth(10)
        barra.draw(win)

    if tecla == "Left":
        if (colIni - 20) > -1:
            colIni = colIni - 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setFill(color_rgb(57, 255, 20))
        barra.setWidth(10)
        barra.draw(win)

    if tecla == "1":
        5
    # Esperar o ser humano reagir
    time.sleep(.03)

if lin == 515 and col > colIni and col < (colIni + tamanho):
    pts += 1
    pontos = Text(Point(400, 575), "Pontos: " + str(pts))
    pontos.setSize(14)
    pontos.setFill("white")
    pontos.draw(win)

    if lin == 550:
        chances.undraw()
        chan -= 1
        chances = Text(Point(100, 575), "Chances = " + str(chan))
        chances.setFace()
        chances.setSize(14)
        chances.setFill("white")
        chances.draw(win)
win.close()

