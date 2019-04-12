print("Bienvenido a Muerte Lenta")
numP = int(input("Ingrese el numero de personas en la mesa: "))

while True:

    acum=0
    ch=0
    cp=0
    cs=0
    cc=0

    for i in range(numP):

        f = input("Ingrese H - Hamburguesa, P - Perro, S - Salchipapa, C - Chorizos:")

        if f == 'H' or f=='h':
            acum = acum + 10000
            ch=ch+1
            
        elif f == 'P' or f=='p':
            acum = acum + 8000
            cp=cp+1

        elif f == 'S' or f=='s':        
            acum = acum + 6000
            cs=cs+1        

        elif f == 'C' or f=='c':       
            acum = acum + 7000
            cc=cc+1
                
        else:
            print("Opcion no válida, ingrese nuevamente una opcion valida")

            
    if acum > 20000:
        acum = acum * 0.9
        print("Por su compra mayor a 20000 se hizo un descuento del 10%, su valor a pagar es: " + str(acum) )

    prop=input("¿Desea incluir propina S/N?")

    if prop=='S' or prop=='s':
        acum = acum + (acum*0.1)


    if ch >= 2 or cp >= 2 or cs >= 2 or cc >= 2:
        acum = acum * 0.95
        print("Por llevar dos productos iguales recibe un descuento del 5%, "+str(acum))


    print("Su valor a pagar es de: " + str(acum))


    rta = input("Atender otra mesa? S/N")
    if rta == 'N':
        break