#9.	Url’s
import re
estracto= 'Este texto sera el usado para los ejercicios "es" posible que se use y se repita pffks jhassda jss http://google.com Mcdonals dancuso125@hotmail.com   Mjahr fin del comunicadoo 22/10/20'
patron=r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)