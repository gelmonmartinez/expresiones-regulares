#5.	Ip’s
import re
estracto = 'Encontrar este metodo, apesar de que hay otros con archivos, por ello pondre un enlace https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_Expressions, direccion ip 192.169.49.5, 192.168.49.6, 192.167.49.3 mi codigo postal 87776 9841465270'
patron=r'(\d+\d+.\d+\.\d+.\d+)'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)