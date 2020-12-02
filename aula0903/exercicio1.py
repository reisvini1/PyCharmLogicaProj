# Calculando a aprovação de um aluno sendo a média = 5

# Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2

# Saída
if media >= 5:
    print("O aluno está aprovado com média", media)
else:
    print("O aluno está reprovado com média", media)
