import numpy as np
import pandas as pd
import copy
import itertools

def duplicado(nums):
    dup = [x for i, x in enumerate(nums) if x in nums[:i]]
    return dup

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
print("D:")
print(d)

x=[]
x.append(b)
k=1
#for z in range(1):
for z in range(len(b)):
    
    products=x[0]
    for i in range(len(x)-1):
        products = list(itertools.product(products,x[i+1]))
    for i in range(len(products)):
        string=str(products[i])
        string = string.replace("(","").replace(")","").replace(",","").replace(" ",", ")
        tupla=tuple(map(float, string.split(', ')))
        products[i]=tupla
        
    #print(products)
    for tupla in products:

        if len(duplicado(tupla))==0 and list(tupla)==sorted(tupla):
            daux=[]
            daux.append(d0)
            for element in tupla:
                daux.append(element)
            daux.append(dn)
            #print("daux")
            #print(daux)
            d=[]
            for indice in range(len(daux)-1):
                d.append([daux[indice],daux[indice+1]])    
            print("D:")
            print(d)
            #aqui se creara matriz quanta y se calculara caim

            quanta=np.zeros((len(clas),len(d)+1))
            for i in range(len(clas)):
                quanta[i][0]=clas[i]
            #print(quanta)

            for indice in range(len(dv)):
                cl=data.iloc[indice]['clase']
                #print(cl)
                v=data.iloc[indice]['valor']
                #print(v)
                
                for classe in range(len(clas)):
                    if cl==quanta[classe][0]:
                        for intervalo in range(len(d)):
                            lims=d[intervalo]
                            liminf=lims[0]
                            limsup=lims[1]
                            #print("limites:")
                            #print(liminf)
                            #print(limsup)
                            if intervalo==0:
                                if liminf<=v and v<=limsup:
                                    quanta[classe][intervalo+1]+=1
                            
                            else:
                                if liminf<v and v<=limsup:
                                    quanta[classe][intervalo+1]+=1
            print(quanta)
    
    popaux=copy.deepcopy(x[z])
    #elimina el ultimo elemento de cada tupla
    for w in range(z+1):
        x[w].pop()

    #quita el primer elemento de la ultima tupla y pega esa nueva tupla al final de la lista
    popaux.pop(0)
    x.append(popaux)
    
    k+=1  #agregar funcion de paro de k<s  