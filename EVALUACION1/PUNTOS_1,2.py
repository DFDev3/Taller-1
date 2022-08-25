import os 
import time
import math
#______________________________________________
#           FUNCIONES DE OPERACIONES
#______________________________________________
def UNION(A:set,B:set):
    C=A|B
    return C
def INTERSECCION(A:set,B:set):
    C=A&B
    return C
def DIFERENCIA(A:set,B:set):
    C=A-B
    return C
def DIFSIM(A:set,B:set):
    C=A^B
    return C
isActive=True
headers=["Operaciones Conjuntos","Permutaciones y Combinaciones","Salir\n"]


while isActive:
    for i in range(len(headers)):
        print(f"{i+1} - {headers[i]}")
    try:
        op=int(input(")_"))
    except:
        op=0
        print("\nElección inválida\n")
    else:
        if op==1:
            #------------DECLARACIÓN DE CONJUNTOS------------
            A=set()
            B={0,2,4,6,12,24,28}
            C=set()
            D={2,3,5,7,11,13,17,19,23,29,31,37}
            for i in range(10,30):
                A.add(i)
            for i in range(0,46):
                if i%4==2:
                    C.add(i)
            print(f"\nCONJUNTOS\n\nA: {A}\nB: {B}\nC: {C}\nD: {D}\n\n_________")
            
            #------------OPERACIONES DE CONJUNTOS------------
            E:set=(DIFSIM(DIFERENCIA(A,C),INTERSECCION(B,D)))
            F:set=(DIFERENCIA(DIFSIM(INTERSECCION(B,D),C),UNION(A,D)))
            G:set=(INTERSECCION(INTERSECCION(A,B),C))
            H:set=(UNION(DIFERENCIA(A,C),DIFERENCIA(B,D)))
            I:set=(UNION(G,H))
            
            #------------RESPUESTAS------------
            print(f"\n\nRESPUESTAS\n\n")
            print(f"OPERACIÓN 1: (A-C)^(B&D)                 RESPUESTA: {E}")
            print(f"OPERACIÓN 2: ((B&D)^C)-(A|D)             RESPUESTA: {F}")
            print(f"OPERACIÓN 3: (A&B&C)|((A-C)|(B-D))       RESPUESTA: {I}")
            
        elif op==2:
            
            #------------FACTORIALES------------
            f15=math.factorial(15)
            f10=math.factorial(10)
            f5=math.factorial(5)
            f9=math.factorial(9)
            f6=math.factorial(6)
            f4=math.factorial(4)
            f3=math.factorial(3)
            f2=math.factorial(2)
            #------------COMBINACIONES Y PERMUTACIONES------------
            dosA=(f15)/(f10*f5)
            dosB_1=(f9)/(f6*f3)
            dosB_2=(f6)/(f4*f2)
            dosB=dosB_1*dosB_2
            dosC=(f15)/(f10)
            print(int(dosA))
            print(int(dosB))
            print(int(dosC))
            
            #------------RESPUESTAS------------
            print(f"2.a)  -     {dosA}")
            print(f"2.b)  -     {dosB}")
            print(f"2.c)  -     {dosC}")
            
        elif op==3:
            isActive=False
