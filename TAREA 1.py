#1.	Todas las palabras que tengan una longitud de 7 o más letras
import re
estracto= 'Me llamo gelmon martinez hernadez, estoy quinto semestre del curso de ingenieria en sistemas practica de python con "Expresiones regulares","de lenguaje y automatas","textos" buscando en internet logre encontrar este metodo, apesar de que hay otros con archivos, por ello pondre un enlace https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_Expressions mi codigo postal 87776 9841465270'

patron=r'(\b\w{7,}\b)'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)