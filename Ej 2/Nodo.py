class Nodo:
    __izquierda=None
    __derecha=None
    __clave=0

    def __init__(self, dato):
        self.__izquierda=None
        self.__derecha=None
        self.__clave=dato

    def setIzquierda(self,izq):
        self.__izquierda=izq
    def setDerecha(self,der):
        self.__derecha=der
    def getIzquierda(self):
        return self.__izquierda
    def getDerecha(self):
        return self.__derecha
    def getClave(self):
        return self.__clave