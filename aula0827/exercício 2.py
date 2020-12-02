# Recebendo um valor em real e convertendo para o dólar e o euro
# Utilizando cotações do dia 27/08/2020
# Dólar = 5,57
# Euro = 6,68

real = float(input("Valor em reais a ser convertido: "))

dolar = real / 5.57
euro = real / 6.68

print("O valor em dólares é: ", dolar)
print("E o valor em euros é: ", euro)
