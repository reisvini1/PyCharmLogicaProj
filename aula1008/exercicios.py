from graphics import *

# Janela
janela = GraphWin("Exercicio", 600, 600)



# Polígono
poli = Polygon(Point(300, 400), Point(350, 450), Point(300, 500), Point(250, 450))
poli.setOutline("blue")
poli.setFill("blue")
poli.draw(janela)

# Oval
oval = Oval(Point(400, 100), Point(200, 40))
oval.setOutline("red")
oval.setFill("red")
oval.draw(janela)

# Textos
text = Text(Point(120, 250), "Qual é o seu nome:")
text.setOutline("black")
text.setSize(18)
text.draw(janela)
text.setText(' ')

inp = Entry(Point(380, 250), 30)
inp.draw(janela)
inp.setFill(color_rgb(230, 230, 230))

ret = Text(Point(100, 300), "")
ret.setOutline("red")
ret.setSize(18)
ret.draw(janela)

# Linhas
for linha in range (0, 600):
    linha = Line(Point(0, 200), Point(599, 200))
    linha.setFill("black")
    linha.draw(janela)
    linha2 = Line(Point(0, 380), Point(599 , 380))
    linha2.setFill("black")
    linha2.draw(janela)


while True:
    janela.getMouse()
    t = Text(Point(100, 350), "Você digitou: ")
    t.setOutline("red")
    t.setSize(18)
    t.draw(janela)
    ret.setText(text.getText())



