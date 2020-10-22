#5.	Ip’s
import re
estracto = 'Me llamo gelmon martinez hernadez, estoy quinto semestre del curso de ingenieria en sistemas practica de python con "Expresiones regulares","de lenguaje y automatas","textos" buscando en internet logre encontrar este metodo, apesar de que hay otros con archivos, por ello pondre un enlace https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_Expressions, direccion ip 192.168.49.5 mi codigo postal 87776 9841465270'
patron=r'(\d+\.\d+\.\d+)'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)