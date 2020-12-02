

# Realizando a descriptografia da cifra de César
print("Realizando a descriptografia da cifra de César")
crip=input("Digite a frase: ")

fraseori=""
for ind in range(0, len(crip)):
    codigo: int = ord(crip[ind])
    codigo -= 2
    novoCaracter = chr(codigo)
    fraseori += novoCaracter

print("A frase descriptografada é")
print(fraseori)