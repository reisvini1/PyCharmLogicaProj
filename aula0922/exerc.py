
lado = int(input("Quantos caracteres no lado do quadrado [10-100]? "))
if lado<10 or lado>100:
  print("Informe um número entre 10 e 100!")
else:
  for linha in range(0, lado):
      print()
      for coluna in range(0, lado):
          if coluna == linha or (linha + coluna) == 9:
           print(" 0 ", end="")
           if linha + coluna == lado -1:
               print(" + ", end="")
          if coluna == linha:
              print(" + ", end="")
          else:
              print(" 0 ", end="")
print()
