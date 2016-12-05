import urllib.request
pagina = urllib.request.urlopen('http://www.dolarhoje.net.br/')
texto = pagina.read().decode('utf8')
dolar = texto[25058:25096]
hoje = texto[10849:10860]
print('cotação realizada no dia',hoje)
print(dolar)
