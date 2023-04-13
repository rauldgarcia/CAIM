import numpy as np
import pandas as pd
import copy

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
baux=copy.deepcopy(b)


for elemento in b:
    #agrega siguiente elemento de b
    #print(daux)
    daux.pop()
    #print(daux)
    daux.append(elemento)
    #print(daux)
    daux.append(dn)
    #print(daux)

    print()
    print("B:")
    print(daux)
    d=[]
    for indice in range(len(daux)-1):
        d.append([daux[indice],daux[indice+1]])    
    #print("D:")
    #print(d)
    #print(len(d))
    

    for j in range(len(d)-1):
        #print("j")
        #print(j)
        try:
            ind=d[j].index(elemento)
            for x in baux:
                
                #print(ind)
                d[j][ind]=x
                d[j+1][ind-1]=x
                print("D:")
                print(d)

        except:
            continue
    baux.pop(0)