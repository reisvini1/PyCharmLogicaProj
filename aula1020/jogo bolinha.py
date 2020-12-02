from graphics import *
import random

# Janela
win = GraphWin("Bolinha ...", 800, 600)
win.setBackground("Black")

# Nome do jogo
jogo=Text(Point(400, 20 ), "~ O JOGO ~")
jogo.setSize(15)
jogo.setStyle("bold")
jogo.setFill(color_rgb(255,255,0))
jogo.draw(win)

# Linha Superior e Inferior
linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(10)
linhaSuperior.setFill("white")
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setFill("white")
linhaInferior.draw(win)

# Círculo Inicial
col = 390
lin = 80
raio = 15
circulo=Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(255,0,127))
circulo.draw(win)

# Barra
colIni = 340
tamanho = 100
barra=Line(Point(colIni, 530), Point(colIni+tamanho, 530))
barra.setFill(color_rgb(57,255,20))
barra.setWidth(10)
barra.draw(win)

# Pontuação
pts = 0
pontos=Text(Point(400, 575), "Pontos: " + str(pts))
pontos.setSize(14)
pontos.setFill("white")
pontos.draw(win)

# Chances
chan = 3
chances=Text(Point(100, 575), "Chances = " + str(chan))
chances.setSize(14)
chances.setFill("white")
chances.draw(win)

# Variavéis
x = 0.05
velocidade=5
bateu = True
continuar = True

# Código
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

  # Colisão barra
  if lin == 515 and col > colIni and col < (colIni+tamanho):
      velocidade = -velocidade
      pontos.undraw()
      pts += 1
      pontos = Text(Point(400, 575), "Pontos: " + str(pts))
      pontos.setSize(14)
      pontos.setFill("white")
      pontos.draw(win)

      # Dificuldade
      if pts >= 1:
          x = 0.04
      if pts >= 2:
          x = 0.03
      if pts >= 3:
          x = 0.02
      if pts >= 4:
          x = 0.01

  # Colisão linha inferior
  if lin == 550:
      chances.undraw()
      chan -= 1
      chances = Text(Point(100, 575), "Chances = " + str(chan))
      chances.setSize(14)
      chances.setFill("white")
      chances.draw(win)

      circulo.undraw()
      col = 390
      lin = 80
      raio = 15
      circulo = Circle(Point(col, lin), raio)
      circulo.setFill(color_rgb(255, 0, 127))
      circulo.draw(win)
      time.sleep(1)

      # Game Over, jogar novamente e sair do jogo
      if chan == 0:
          velocidade = 0
          passo = 0

          gameover=Text(Point(400, 150 ), "GAME OVER")
          gameover.setSize(30)
          gameover.setStyle("bold")
          gameover.setFill(color_rgb(255,255,0))
          gameover.draw(win)

          option = Text(Point(400, 250), "Jogar novamente ?")
          option.setSize(20)
          option.setStyle("bold")
          option.setFill(color_rgb(255, 255, 0))
          option.draw(win)

          op0 = Text(Point(290, 450), "Esc - Sair do jogo")
          op0.setSize(15)
          op0.setStyle("bold")
          op0.setFill(color_rgb(255, 255, 0))
          op0.draw(win)

          op1 = Text(Point(550, 450), "Enter - Jogar novamente")
          op1.setSize(15)
          op1.setStyle("bold")
          op1.setFill(color_rgb(255, 255, 0))
          op1.draw(win)

          # Pontuação Final
          score = Text(Point(400, 350), "Pontuação final :" + str(pts))
          score.setSize(15)
          score.setFill(color_rgb(255, 255, 0))
          score.draw(win)

  # Nova posição do círculo
  circulo.undraw()
  col += passo
  lin += velocidade
  circulo = Circle(Point(col, lin), 15)
  circulo.setFill(color_rgb(255,0,127))
  circulo.draw(win)

  # Movimento horizontal da barra pelas setas direita/esquerda
  tecla = win.checkKey()

  # Sair do joguinho
  if tecla == "Escape":
      continuar = False
      continue

  # Jogar novamente (ENTER)
  if tecla == "Return":
      gameover.undraw()
      option.undraw()
      op0.undraw()
      op1.undraw()
      pontos.undraw()
      score.undraw()
      pts = 0
      pontos = Text(Point(400, 575), "Pontos: " + str(pts))
      pontos.setSize(14)
      pontos.setFill("white")
      pontos.draw(win)

      if pts >= 1:
          x = 0.04
      if pts >= 2:
          x = 0.03
      if pts >= 3:
          x = 0.02
      if pts >= 4:
          x = 0.01

      chances.undraw()
      chan = 3
      chances = Text(Point(100, 575), "Chances = " + str(chan))
      chances.setSize(14)
      chances.setFill("white")
      chances.draw(win)

      velocidade = 5
      bateu = True

  # Tecla direita (RIGHT)
  if tecla == "Right":
      if (colIni + 20) < 701:
          colIni = colIni + 40

      barra.undraw()
      barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
      barra.setFill(color_rgb(57,255,20))
      barra.setWidth(10)
      barra.draw(win)

  # Tecla esquerda (LEFT)
  if tecla == "Left":
      if (colIni - 20) > -1:
          colIni = colIni - 40

      barra.undraw()
      barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
      barra.setFill(color_rgb(57,255,20))
      barra.setWidth(10)
      barra.draw(win)

  # Esperar o ser humano reagir
  if pts == 0:
      x = 0.05
  time.sleep(x)

win.close()
