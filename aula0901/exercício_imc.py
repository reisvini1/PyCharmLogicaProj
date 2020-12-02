# Programa feito para cálculo de IMC com base na altura e peso.

# Entrada de dados
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

# Processamento
IMC = peso
IMC /= altura ** 2

# Saída
print()
print("O seu IMC é de", "%.2f" % IMC, end=" ")

# Condicionais
if IMC < 17:
    print("e isso significa que você está muito abaixo do peso.")
elif 17 <= IMC <= 18.49:
    print("e isso significa que você está abaixo do peso.")
elif 18.5 <= IMC <= 24.99:
    print("e isso significa que você está com o peso normal.")
elif 25 <= IMC <= 29.99:
    print("e isso significa que você está acima do peso.")
elif 30 <= IMC <= 34.99:
    print("e isso significa que você está com obesidade nível I.")
elif 35 <= IMC <= 39.99:
    print("e isso significa que você está com obesidade nível II (severa).")
elif IMC > 40:
    print("e isso significa que você está com obesidade nível III (mórbida).")
