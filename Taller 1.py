#Solicitar dos conjuntos de numeros decimales, preguntar operación, print conjunto resultado y cardinalidad

import os
import time

A=set()
B=set()
header=["SUMA","INTERSECCIÓN","DIFERENCIA","DIFERENCIA SIMÉTRICA"]


print(" # # # # # # # # # # # # # # # # # # # # #  # ")
print(" # # # # # CALCULADORA DE CONJUNTOS # # # # # ")
print(" # # # # # # # # # # # # # # # # # # # # #  # \n\n")

isValid=True
while isValid:
    try:
        CardA=int(input("Ingrese la cantidad de elementos del conjunto A: "))
        CardB=int(input("\nIngrese la cantidad de elementos del conjunto B: "))
    except:
        print("\nTipo de valor inválido\n")
        cardA=0
        cardB=0
        time.sleep(2)
        os.system('cls')
    else:
        isValid=False

print("\nIngrese los elementos del conjunto A: \nRecuerde que deben ser números decimales\n")
i=0
while i!=CardA:
    x=float(input(")_ "))
    A.add(x)
    i+=1
print("\nIngrese los elementos del conjunto B: \nRecuerde que deben ser números decimales\n")
i=0
while i!=CardB:
    x=float(input(")_ "))
    B.add(x)
    i+=1

print("")
for i in range(len(header)):
    print(f"{i+1}  -  {header[i]}")
op=int(input(")_ "))

if op==1:
    C=set()
    for i in A:
        C.add(i)
    for i in B:
        C.add(i)
    print(f"\nEl conjunto resultado es {C}, y su cardinalidad es {len(C)}")
elif op==2:
    C=set()
    D=set()
    for i in A:
        C.add(i)
    for i in B:
        C.add(i)

    for j in C:
        if j in A:
            if j in B:
                D.add(j)
    print(f"\nEl conjunto resultado es {D}, y su cardinalidad es {len(D)}")
elif op==3:
    C=set()
    D=set()
    for i in A:
        C.add(i)
    for i in B:
        C.add(i)
    print("1. A - B")
    print("2. B - A")

    op1=int(input("\n"))

    if op1==1:
        for k in C:
            if k in A:
                if k not in B:
                    D.add(k)
        print(f"\nEl conjunto resultado es {D}, y su cardinalidad es {len(D)}")
    elif op1==2:
        for k in C:
            if k in B:
                if k not in A:
                    D.add(k)
        print(f"\nEl conjunto resultado es {D}, y su cardinalidad es {len(D)}")
elif op==4:
    C=set()
    D=set()
    E=set()
    for i in A:
        C.add(i)
    for i in B:
        C.add(i)
    
    for h in C:
        if h in A:
            if h in B:
                D.add(h)
    
    for i in C:
        if i not in D:
            E.add(int)
    print(f"\nEl conjunto resultado es {E}, y su cardinalidad es {len(E)}")
    




