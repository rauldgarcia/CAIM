import numpy as np
import pandas as pd

data=pd.read_csv('prueba.csv')
print(data)

dataordenada=data.sort_values('valor')
print(dataordenada)

dv=list(dataordenada['valor'])
print("Lista ordenada de valores:")
print(dv)
clases=list(dataordenada['clase'])
clas=list(set(clases)) #crea lista de valores de clase unicos
print("Clases:")
print(clas)

#obtiene limites
d0=dv[0]
dn=dv[-1]

b=[]
for i in range(len(dv)-1):
    b.append(dv[i])
    b.append((dv[i]+dv[i+1])/2)
b.append(dv[-1])
print("B:")
print(b)
b.pop(0)
b.pop()

print()

daux=[d0,dn]
d=[[d0,dn]]
globalcaim=0
k=1
print("D:")
print(d)

for elemento in b:
    #agrega siguiente elemento de b
    daux.pop()
    daux.append(elemento)
    daux.append(dn)
    print("B:")
    print(daux)
    d=[]
    for indice in range(len(daux)-1):
        d.append([daux[indice],daux[indice+1]])    
    print("D:")
    print(d)