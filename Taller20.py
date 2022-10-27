import numpy as np 
import os
casicero = 1e-15 
def GAUSS(A,B):
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    for i in range(0,n-1,1):
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        if (dondemax !=0):
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)
    ltfila = n-1
    ultcolumna = m-1
    for i in range(ltfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])
    return [X[0][0],X[0][1],X[0][2]]

x=[0,1,2,3,4,5,6]
y=[-0.9,0,2,4.5,8.3,13,13,18]
sum_y=0
sum_x=0
sum_x2=0
sum_x3=0
sum_x4=0
sum_xy=0
sum_x2y=0
n=len(x)
for i in range(len(x)):
    sum_x+=x[i]
    sum_x2+=x[i]*x[i]
    sum_x3+=x[i]*x[i]*x[i]
    sum_x4+=x[i]*x[i]*x[i]*x[i]
    sum_y+=y[i]
    sum_xy+=x[i]*y[i]
    sum_x2y+=x[i]*x[i]*y[i]

A = np.array([[n,sum_x,sum_x2],
             [sum_x,sum_x2,sum_x3],
             [sum_x2,sum_x3,sum_x4]])
B = np.array([[sum_y],
             [sum_xy],
             [sum_x2y]])
    
print(f"La función resultante es y = {GAUSS(A,B)[0]}x1 + {GAUSS(A,B)[1]}x2 + {GAUSS(A,B)[2]}x3 + e")
