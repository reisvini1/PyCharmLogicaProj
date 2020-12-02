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
notafinal = (nota1 + (nota2*1.5) + (nota3*2)) / 4.5

# Retorno sobre a menção do aluno
print()
if notafinal == 0:
    print("A menção do aluno foi SR")
elif 0.1 <= notafinal < 1.9:
    print("A menção do aluno foi II")
elif 2 <= notafinal < 4.9:
    print("A menção do aluno foi MI")
elif 5 <= notafinal < 6.9:
    print("A menção do aluno foi MM")
elif 7 <= notafinal < 8.9:
    print("A menção do aluno foi MS")
elif notafinal >= 9:
    print("A menção do aluno foi SS")
print("A nota final foi de:", "%.2f" % notafinal)
