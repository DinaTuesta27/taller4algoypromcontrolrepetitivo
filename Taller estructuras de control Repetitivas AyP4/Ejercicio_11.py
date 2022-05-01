continuar=input("¿Desea seguir?:")

while (continuar=="si"):
    conlicor=input("¿Consume licor?:")
    licorpref=input("Licor favorito:")
    edad=int(input("Digite su edad:"))
    sexo=input("Digite su sexo:")
    cont=0
    cont2=0
    cont3=0
    cont4=0
    cont5=0
    cont6=0
    cond=0
    condm=0
    cons=0
    consh=0
    if(conlicor=="si"):
        if(licorpref=="Aguardiente"):
            cont=cont+1
            print("Aguardiente:",cont)
        elif(licorpref=="Ron"):
            cont2=cont2+1
            print("Ron:",cont2)
        elif(licorpref=="cerveza"):
            cont3=cont3+1
            print("Cerveza:",cont3)
        elif(licorpref=="Tequila"):
            cont4=cont4+1
            print("Tequila:",cont4)
        elif(licorpref=="whisky"):
            cont5=cont5+1
            print("Whisky:",cont5)
        elif(licorpref=="Ninguno"):
            cont6=cont6+1
            print("Otro:",cont6)
    elif(edad>=18):
        cond=cond+1
        print("Mayor de edad.",cond)
    else:
        condm=condm+1
        print("Menor de edad.",condm)
    if(sexo=="mujer"):
        cons=cons+1
        print("Mujer",cons)
    else:
        consh=consh+1
        print("Hombre",consh)
    continuar=input("¿Desea seguir?:")
else:
    if(continuar=="no"):
       print("Fin")
       
    

