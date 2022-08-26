class Pila:
    __tope1 = None
    __tope2 = None
    __tope3 = None
    __elemento1 = None
    __elemento2 = None
    __elemento3 = None

    def __init__(self):
        self.__tope1 = -1
        self.__tope2 = -1
        self.__tope3 = -1
        self.__elemento1 = []
        self.__elemento2 = []
        self.__elemento3 = []

    def Vacio1(self):
        return (self.__tope1 == -1)
    
    def Vacio2(self):
        return (self.__tope2 == -1)
    
    def Vacio3(self):
        return (self.__tope3 == -1)
    
    def Insertar1(self, x):
        self.__tope1 += 1
        self.__elemento1.append(x)
        return (x)
 
    def Insertar2(self, x):
        self.__tope2 += 1
        self.__elemento2.append(x)
        return (x)

    def Insertar3(self, x):
        self.__tope3 += 1
        self.__elemento3.append(x)
        return (x)

    def Suprimir1(self):
        if (self.Vacio1()):
            print("\nLa Pila 1 esta vacia")
            return 0
        else:
            self.__tope1 -= 1
            x = self.__elemento1.pop(self.__tope1)
            return x

    def Suprimir2(self):
        if (self.Vacio2()):
            print("\nLa Pila 2 esta vacia")
            return 0
        else:
            self.__tope2 -= 1
            x = self.__elemento2.pop(self.__tope2)
            return x

    def Suprimir3(self):
        if (self.Vacio3()):
            print("\nLa Pila 3 esta vacia")
            return 0
        else:
            self.__tope3 -= 1
            x = self.__elemento3.pop(self.__tope2)
            return x

    def Mostrar(self):
        if not(self.Vacio1()):
            i = self.__tope1
            while (i >= 0):
                print(('[{}]        [{}]        [{}]').format(self.__elemento1[i],self.__elemento2[i],self.__elemento3[i]))
                i -= 1
