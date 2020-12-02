# Calculando se um salário está nos parâmetros da lei
# Salário mínimo = R$ 1045

# Entrada
salario = int(input("Digite o salário recebido: "))

# Processamento e saída
salariomin = 1045
if salario >= salariomin:
    print("O salário informado no valor de R$", salario , "está de acordo com a legislação brasileira.")
else:
    print("O salário informado no valor de R$", salario, "não está de acordo com a legislação brasileira")
