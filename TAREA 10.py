#10.	Código postal
import re
estracto= 'Me llamo gelmon martinez hernadez,  87776, a veces 87780 9841465270'

patron=r'([0-9]{5})'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)