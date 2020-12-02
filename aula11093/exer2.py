import os

diretorio = os.listdir("c:\\")

#Código
arq = open('c:\\temp\\diretorio.html', 'w')
arq.write('<html><head><title>Listagem de diretório</title></head>')
arq.write('<body><ul>')
for nome in diretorio:
   arq.write ('<li>{}</li>'.format(nome))

arq.write('</ul></body></html>')

arq.close()
