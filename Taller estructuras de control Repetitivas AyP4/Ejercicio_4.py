#Entrada
suma=0
for i in range(6,62,5):#i empieza en 1 y saldran 12 resultados
    print(i)
    #print(f"{6+(i-1)*5}") #Van las condiciones para que salga la suceción
    if(i<600):
        suma=suma+i #la operación esta dentro de la condición e imprime eso
                 #por eso necesita otra cond.
        print(suma)
    else:
        break
        


