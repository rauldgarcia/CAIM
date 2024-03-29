import numpy as np
import pandas as pd
import copy
import itertools
import time
inicio=time.time()

def duplicado(nums):
    dup = [x for i, x in enumerate(nums) if x in nums[:i]]
    return dup

data=pd.read_csv('iris.csv')
#print(data)

names=data.columns.values
print(names)
print(names[0])

listclas=data[names[-1]].tolist()
lclas=list(set(listclas))
#print(listclas)
print(lclas)

for numero in range(len(data)):
    for nombre in range(len(lclas)):
        if data[names[-1]][numero]==lclas[nombre]:
           data[names[-1]][numero]=nombre
           break

#print(data) 

for atributo in range(len(names)-1):
    print(names[atributo])

    dataordenada=data.sort_values(names[atributo])
    #print(dataordenada)

    da=list(dataordenada[names[atributo]])
    #print(da)
    dv=list(set(da))
    dv.sort()
    #print("Lista ordenada de valores:")
    #print(dv)
    clases=list(dataordenada[names[-1]])
    clas=list(set(clases)) #crea lista de valores de clase unicos
    #print("Clases:")
    #print(clas)

    #obtiene limites
    d0=dv[0]
    dn=dv[-1]

    b=[]
    for i in range(len(dv)-1):
        b.append(dv[i])
        b.append((dv[i]+dv[i+1])/2)
    b.append(dv[-1])
    #print("B:")
    #print(len(b))

    b.pop(0)
    b.pop()

    daux=[d0,dn]
    d=[[d0,dn]]
    globalcaim=0
    #print("D:")
    #print(d)

    x=[]
    x.append(b)
    k=1

    mejorcaim=[]
    globalcaim=0
    #for z in range(1):
    for z in range(len(b)):
        if k>=len(clas):
            break
        
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
                d=[]
                for indice in range(len(daux)-1):
                    d.append([daux[indice],daux[indice+1]])    
                #print("D:")
                #print(d)

                quanta=np.zeros((len(clas),len(d)+1))
                for i in range(len(clas)):
                    quanta[i][0]=clas[i]

                for indice in range(len(dv)):
                    cl=data.iloc[indice][names[-1]]
                    v=data.iloc[indice][names[atributo]]
                    
                    for classe in range(len(clas)):
                        if cl==quanta[classe][0]:
                            for intervalo in range(len(d)):
                                lims=d[intervalo]
                                liminf=lims[0]
                                limsup=lims[1]
                                if intervalo==0:
                                    if liminf<=v and v<=limsup:
                                        quanta[classe][intervalo+1]+=1
                                        break
                                
                                else:
                                    if liminf<v and v<=limsup:
                                        quanta[classe][intervalo+1]+=1
                                        break
                quanta=np.delete(quanta,0,axis=1)
                #print("Quanta:")
                #print(quanta)

                #sr=np.sum(quanta, axis=1) #suma renglon
                sc=np.sum(quanta, axis=0) #suma columna
                maximos=np.argmax(quanta,axis=0) #indice donde se encuentra el valor mas grande
            
                suma=0   
                for i in range(len(d)-1):
                    if sc[i]!=0:
                        suma=suma+((quanta[i][maximos[i]]**2)/sc[i])
                caim=suma/len(d)
                #print("Caim:")
                #print(caim)

                if caim>globalcaim:
                    globalcaim=copy.deepcopy(caim)
                    mejorcaim=copy.deepcopy(d)
        
        popaux=copy.deepcopy(x[z])
        #elimina el ultimo elemento de cada tupla
        for w in range(z+1):
            x[w].pop()

        #quita el primer elemento de la ultima tupla y pega esa nueva tupla al final de la lista
        popaux.pop(0)
        x.append(popaux)
        
        k+=1  

    print("El mejor intervalo de discretización es:")
    print(mejorcaim)
    
    for ejemplo in range(len(data)):
        valor=data[names[atributo]][ejemplo]
        for rango in range(len(mejorcaim)):
            limites=mejorcaim[rango]
            inf=limites[0]
            sup=limites[1]

            if rango==0:
               if inf<=valor and valor<=sup:
                    data[names[atributo]][ejemplo]='clase'+str(rango)
                    break

            else:
                if inf<valor and valor<=sup:
                    data[names[atributo]][ejemplo]='clase'+str(rango)
                    break

for numero in range(len(data)):
    for nombre in range(len(lclas)):
        if data[names[-1]][numero]==nombre:
           data[names[-1]][numero]=lclas[nombre]
           break

print("La data discretizada es:")
print(data)
print("El tiempo de ejecución es:")
fin=time.time()
print(fin-inicio)
data.to_csv('pruebanew.csv')