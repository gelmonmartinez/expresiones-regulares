#8.	Correos electrónicos.
import re
estracto=  'Este texto sera el usado para los ejercicios "es" posible que se use y se repita pffks jhassda jss http://google.com Mcdonals dancuso125@hotmail.com   Mjahr fin del comunicadoo 22/10/20'
patron=r'[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)