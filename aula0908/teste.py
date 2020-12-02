# Resultados e notas dos alunos

# Entrada de notas
nota1 = float(input("Nota 1 do aluno: "))
while nota1 < 0 or nota1 > 10:
    print("Valor inválido, digite novamente")
    nota1 = float(input("Nota 1 do aluno: "))

nota2 = float(input("Nota 2 do aluno: "))
while nota2 < 0 or nota2 > 10:
    print("Valor inválido, digite novamente")
    nota2 = float(input("Nota 2 do aluno: "))

nota3 = float(input("Nota 3 do aluno: "))
while nota3 < 0 or nota3 > 10:
    print("Valor inválido, digite novamente")
    nota3 = float(input("Nota 3 do aluno: "))

# Médias de notas
notafinal = (nota1 + nota2 + nota3) / 3

# Retorno sobre aprovação e notas
print()
print("A nota final do aluno foi de ", notafinal)
print()

if notafinal < 7:
    print("Esse aluno foi reprovado por possuir média menor que 7.")
elif notafinal >= 7:
    print("Esse aluno está aprovado!")
