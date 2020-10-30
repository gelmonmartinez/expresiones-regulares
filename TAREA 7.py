#7.	Telefonos
import re
estracto=  'Me llamo gelmon martinez hernadez, estoy quinto semestre del curso de ingenieria en sistemas mi 9841465270'
patron=r'([0-9]{10})'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)