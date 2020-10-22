# 3.	Las palabras que inicien con “M” donde la segunda letra no sea vocal
import re
estracto = 'Este texto sera el usado para los ejercicios "es" posible que se use y se repita pffks jhassda jss http://google.com Mcdonals dancuso125@hotmail.com   Mjahr fin del comunicadoo 22/10/20'
patron=r'([Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).)'
resultado=re.findall(patron, estracto)
print(len(resultado)) 
print ()
for p in resultado:
    print(p)


