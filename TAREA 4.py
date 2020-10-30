#4.	Expresiones encerradas entre comillas ""
import re
estracto='Me llamo "gelmon" "martinez" hernadez, "estoy" quinto semestre del "curso" de ingenieria en sistemas practica de python con "Expresiones regulares","de lenguaje y automatas","textos" buscando en internet logre encontrar este metodo, apesar de que hay otros con archivos.'

patron=r'"(.*?)"'
resultado=re.findall(patron, estracto)
 
print (resultado)
print()
for p in resultado:
    print(p)