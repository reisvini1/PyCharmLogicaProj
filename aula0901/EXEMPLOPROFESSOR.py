# Entrada de dados
valor = float(input("Qual o valor? "))
porc = float(input("Qual o desconto (0-100%)? "))



# Processamento
# desc = (valor * porc) / 100

desc = valor
desc *= porc
desc /= 100

valorFinal = valor
valorFinal -= desc

# Saída
print ()
print ("Valor Bruto:", valor)
print ("Desconto (", porc, " %%): %.2f" % desc)
print ("Valor Final:", "%.2f" % valorFinal)