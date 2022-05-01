#Entrada
print("MUITO OBRIGADO")
n=int(input())
#Caja negra
while(n>4):
    n=int(input())
contador=0
contador2=0
contador3=0
while(n<4 and n>=1):
    if(n==1):
        contador=contador+1
        print("Alcool:",contador)
        n=int(input())
    elif(n==2):
        contador2=contador2+1
        print("Gasolina:",contador2)
        n=int(input())
    elif(n==3):
        contador3=contador3+1
        print("Diesel:",contador3)
        n=int(input())
    else:
        print(" ")
else:
    n=int(input())




    
