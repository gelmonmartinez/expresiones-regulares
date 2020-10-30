#6.	Horas
import re
estracto= 'Me llamo gelmon martinez hernadez y son las 7:45 estoy quinto semestre del curso de ingenieria en sistemas y tengo clases a las 8:00, juego un rato a las 7:32 y me voy a domir hasta que dan la 1:45'
patron=r'(([01]?[0-9]):[0-5][0-9])'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)