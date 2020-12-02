# Resultados e notas dos alunos

# Entrada de notas
nota1 = float(input("Nota 1 do aluno: "))
if nota1 < 0 or nota1 > 10:
    print("Valor inválido")
while
nota2 = float(input("Nota 2 do aluno: "))
if nota2 < 0 or nota2 > 10:
    print("Valor inválido")

nota3 = float(input("Nota 3 do aluno: "))
if nota3 < 0 or nota3 > 10:
    print("Valor inválido")

# Médias de notas
notafinal = (nota1 + nota2 + nota3) / 3

# Retorno sobre aprovação e notas

print("A nota final do aluno foi de ", notafinal)

if notafinal < 7:
    print("Esse aluno foi reprovado por possuir média menor que 7.")
elif notafinal >= 7:
    print("Esse aluno está aprovado!")
