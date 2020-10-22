#2. Expresiones que NO finalicen con una vocal.
import re
estracto= 'Este texto sera el usado para los ejercicios "es" posible que se use y se repita pffks jhassda jss http://google.com Mcdonals dancuso125@hotmail.com   Mjahr fin del comunicadoo 22/10/20'

patron=r'(([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]){3,7})'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)

