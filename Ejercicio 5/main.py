from pila import Pila

if __name__ == "__main__":
    #presentacion
    print("\nBienvenido al juego 'TORRES DE HANOI'")
    cant = int(input('\nIngrese la cantidad de elementos con la que desea jugar:'))

    #variables
    unaPila1 = Pila(cant)
    unaPila2 = Pila(cant)
    unaPila3 = Pila(cant)
    arreP = [unaPila1, unaPila2, unaPila3]
    x = cant
    cantMov = 0
    
    #cargo la primera torre
    for i in range(cant):
        arreP[0].insertar(x)
        x -= 1
    
    #comienza el juego
    print('\nComencemos!')
    print('\n-----0-----0-----0-----0-----0-----0-----')

    #muestra las torres
    for i in range(len(arreP)):
        print("\nTorre {}".format(i+1))
        arreP[i].mostrar()

    while not arreP[2].lleno():
        origen = int(input('\nIngrese la torre en donde quiere retirar el elemento:'))
        destino = int(input('\nIngrese la torre en donde quiere colocar el elemento:'))

        #movimiento
        if not arreP[origen-1].vacio():
            if (arreP[destino-1].vacio()) or (arreP[destino-1].retUltimo() > arreP[origen-1].retUltimo()): #revisa si la torre destino esta vacia o si tiene un elemento manor
                arreP[destino-1].insertar(arreP[origen-1].suprimir())
                cantMov += 1
                
                #muestra las torres
                print('\n-----0-----0-----0-----0-----0-----0-----')
                for i in range(len(arreP)):
                    print("\nPila {}".format(i+1))
                    arreP[i].mostrar()

            else:
                print('\nLa ficha de la Torre {} es mas pequeña que la ficha de la Torre{}'.format(origen, destino))
        else:
            print('\nNo se pudo realizar el movimiento, la Torre {} se encuentra vacia'.format(origen))
    
    #termina
    print('\nFelicidades usted completo el juego utilizando {} cantidad de elementos en {} movimientos'. format(cant, cantMov))
