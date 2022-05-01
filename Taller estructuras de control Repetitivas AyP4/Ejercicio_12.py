#Entrada
cant=int(input("Digite cantidad de estudiantes: "))
PuntM=0 #Puntaje mayor
Puntm=0 #Puntaje menor
prom=0
for i in range(1,cant+1):
    Nom=str(input("Dijite el nombre del estudiante: "))
    Punt=float(input("Digite nota del estudiante:"))
    if(Punt<=Puntm):
        Puntm=Punt
    elif(PuntM<=Punt):
        PuntM=Punt
    elif(Punt>=0):
        prom=i+Punt

    
#Caja negra
print("El nombre del estudiantes es:",Nom)
print("El promedio es:",prom/cant)
print("El puntaje más alto:",PuntM)
print("El puntaje más bajo:",Puntm)