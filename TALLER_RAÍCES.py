import os
isActive=True

def raiz(n):
    x = n / 2
    for i in range(20):
        if x * x  == n:
            return x 
        else: 
            x = (x + (n/x)) / 2
    return x


while isActive:
    os.system('cls')
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n# # # # # # # # CALCULADORA DE RAÍCES # # # # # # # # # #\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    base=int(input("\n\nIngrese el número cuya raíz cuadrada desea conocer: "))
    if base <= 0:
        print("\n\nEl valor ingresado es negativo, y no tiene raíz cuadrada\n\n")
    else:
        print(f"\n\n El resultado es {raiz(base)}\n\n Desea calcular otra raíz?\n\n")
    isActive=bool(input("(S) para Si, Enter para salir de la calculadora: _"))
