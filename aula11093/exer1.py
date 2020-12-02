
def principal():
   num = int(input("Quer gerar tabuada de? "))

   arq = open('c:\\temp\\tabuada.txt', 'w')

   for fator in range(11):
       mult = num * fator
       arq.write('{} x {} = {}\r'.format(num, fator, mult))
   arq.close()
   print ('Arquivo gerado')

principal()
