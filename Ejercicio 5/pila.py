import numpy as np

class Pila:
    __cant = 0 
    __tope = -1

    def __init__(self, cant):
        self.__item = np.empty(cant, dtype = int)
        self.__tope = -1
        self.__cant = cant

    def retUltimo(self):
        return self.__item[self.__tope]

    def vacio(self):
        return (self.__tope == -1)

    def lleno(self):
        return (self.__tope == self.__cant-1)

    def insertar(self, x):
        if (self.__tope < self.__cant-1):
            self.__tope += 1
            self.__item[self.__tope] = x
            return x
        else: 
            print("\nLa pila esta llena")

    def suprimir (self):
        if (self.vacio()):
            print("\nLa pila esta vacia")
        else:
            x = self.__item[self.__tope]
            self.__tope -= 1
            return x

    def mostrar (self):
        if not (self.vacio()):
            i = self.__tope
            j = self.__cant-1

            while (j != self.__tope):
                print("[0]")
                j -= 1

            while (i >= 0):
                print("[{}]".format(self.__item[i]))
                i -= 1
        else:
            i = self.__cant-1
            while (i >= 0):
                print("[0]")
                i -= 1