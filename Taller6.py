import math 
import os
mcl=2
i=0
cosenos=[]
print("# # # # # # # # # # # # # # # # # # # # # # # #\n# # # CALCULADORA DE VALOR APROXIMADO # # # # #\n# # # # # # # # # # # # # # # # # # # # # # # #\n\n")

ang=float(input("Ingrese un angulo en radianes: "))
Es=math.cos(ang)*(10**-8) * 100 #9.210609940028851e-07
Ea=100000
cosI=1
cosenos.append(cosI)

while Ea>=Es:
    fracc=(ang**mcl)/math.factorial(mcl)
    if i%2==0:
        fracc=fracc*-1
    cosN=cosenos[i]+fracc
    i+=1
    mcl+=2
    cosenos.append(cosN)
    # print(f"{i}\n")
    # print(f"#          {cosenos}\n")
    # print(f"#          {cosenos[i]}\n")
    Ea=abs((cosenos[i]-cosenos[i-1])/cosenos[i])*100
    # print(f"{Ea}%")
print("\n______________________________________________________\nPENSANDO...\n")
os.system('pause')

print(f"\n\n\nVALOR: {cosenos[i]}\n\nERROR: {Ea}\n\n")
