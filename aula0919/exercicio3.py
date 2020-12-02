print("Criptografia personalizada. Deslocamento ASC de +1 e troca de posição dos caracteres")
print()
print("Informe uma frase:")
frase = input()

qtd = len(frase)

if (qtd==0):
  print ("Informe uma frase por favor")
else:
  cripto=""
  for ind in range(0, qtd):
      codigo=ord(frase[ind])
      codigo+=1
      novoCaracter=chr(codigo)
      cripto+=novoCaracter

  print("Intermediário:", cripto)

  metade = int(qtd / 2)
  troca = ""
  for ind in range(0, metade):
      troca += cripto[ind]
      troca += cripto[qtd - ind - 1]
  if (qtd % 2) == 1:
      troca += cripto[metade]

  print("Criptografia final:", troca)

