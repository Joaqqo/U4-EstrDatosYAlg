from Nodo import Nodo

class ABB:
    __raiz=None

    def __init__(self, raiz):
        self.__raiz= Nodo(raiz)

    def getRaiz(self):
        return self.__raiz

    def Insertar(self, clave, raiz): #Raíz sería una subraíz
        #nodo=Nodo(clave)
        if raiz.getClave() == clave:
            print("Error en la inserción")
        else:
            if raiz.getClave() > clave:
                if raiz.getIzquierda() is None:
                    nodo=Nodo(clave)
                    raiz.setIzquierda(nodo)
                    print("Se insertó en la izquierda.")
                else:
                    self.Insertar(clave, raiz.getIzquierda())
            elif raiz.getClave() < clave:
                if raiz.getDerecha() is None:
                    nodo=Nodo(clave)
                    raiz.setDerecha(nodo)
                    print("Se insertó en la derecha.")
                else:
                    self.Insertar(clave, raiz.getDerecha())

    def Frontera(self, raiz):
        if raiz is not None:
            if raiz.getDerecha() is None and raiz.getIzquierda() is None:
                print(raiz.getClave(), end=", ")
            self.Frontera(raiz.getIzquierda())
            self.Frontera(raiz.getDerecha())


    def Preorden(self, raiz):
        if raiz is not None:
            print(raiz.getClave(), end=", ")
            self.Preorden(raiz.getIzquierda())
            self.Preorden(raiz.getDerecha())


