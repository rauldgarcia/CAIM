dv=[0.2, 0.1, 1.4, 2.5, 1.8, 2.2, 1.3, 2.1, 1.9, 1.5]

dv.sort()

d0=dv[0]
dn=dv[-1]

b=[]
print(b)
for i in range(len(dv)-1):
    b.append(dv[i])
    b.append((dv[i]+dv[i+1])/2)
b.append(dv[-1])
print(b)
