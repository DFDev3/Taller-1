import math 
import os

isActive=True
while isActive:
    print("_____________________________________________________________________________________________________________________________________________________")
    print("# # # # # # # # # # # # # # # # # # # # # # # #\n# # # CALCULADORA DE VALOR APROXIMADO # # # # #\n# # # # # # # # # # # # # # # # # # # # # # # #\n\n")  
    print("1 - SERIE DE MACLAURIN #1\n2 - SERIE DE MACLAURIN #2\n3 - Salir")
    op=int(input(")_ "))

    if op==1:
        mcl=2
        i=0
        x=0.85
        eulers=[]
        print("# # # # # # # # # # # # # # # # # # # # # # # #\n# # # CALCULADORA DE VALOR APROXIMADO # # # # #\n# # # # # # # # # # # # # # # # # # # # # # # #\n\n")

        Es=0.5*(10**-8) * 100 #5e-07
        Ea=100000
        eulI=1-x
        eulers.append(eulI)

        while Ea>=Es:
            fracc=(x**mcl)/math.factorial(mcl)
            if i%2!=0:
                fracc=fracc*-1
            eulN=eulers[i]+fracc
            i+=1
            mcl+=1
            eulers.append(eulN)
            # print(f"{i}\n")
            # print(f"#          {cosenos}\n")
            # print(f"#          {cosenos[i]}\n")
            Ea=abs((eulers[i]-eulers[i-1])/eulers[i])*100
            # print(f"{Ea}%")
        print("\n______________________________________________________\nPENSANDO...\n")
        os.system('pause')

        print(f"\n\n\nVALOR: {eulers[i]}\n\nERROR: {Ea}\n\nITERACIONES: {i}\n\nÚLTIMO EA: {Ea}")
    elif op==2:
        mcl=2
        i=0
        euler=[]
        x=0.85
        print("# # # # # # # # # # # # # # # # # # # # # # # #\n# # # CALCULADORA DE VALOR APROXIMADO # # # # #\n# # # # # # # # # # # # # # # # # # # # # # # #\n\n")
        Es=0.5*(10**-8) * 100 
        Ea=100000
        eulI=1+x
        euler.append(eulI)

        while Ea>=Es:
            fracc=(x**mcl)/math.factorial(mcl)
            eulN=euler[i]+fracc
            i+=1
            mcl+=1
            euler.append(eulN)
            # print(f"{i}\n")
            # print(f"#          {cosenos}\n")
            # print(f"#          {cosenos[i]}\n")
            Ea=abs((euler[i]-euler[i-1])/euler[i])*100
            # print(f"{Ea}%")
        print("\n______________________________________________________\nPENSANDO...\n")
        os.system('pause')
        r=1/euler[i]
        print(f"\n\n\nVALOR: {r}\n\nERROR: {Ea}\n\nITERACIONES: {i}\n\nÚLTIMO EA: {Ea}")
    elif op==3:
        print("HASTA PRONTO")
        isActive=False