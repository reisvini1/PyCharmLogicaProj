# Lista com números (for e range)

# Entrada de dados
ni = int(input("Qual o número inicial? "))
nf = int(input("Qual o número final? "))
ps = int(input("Qual o passo? "))

# Variáveis
if ni < 0 or nf < 0 or ps < 0:
    print()
    print("Digite um valor maior que 0.")
elif ni > nf:
    print()
    print("O número final deve ser maior que o inicial.")

# Saída
for saida in range(ni, nf, ps):
    print(saida)
