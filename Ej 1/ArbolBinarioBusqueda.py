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

    def maxIzquierda(self, padre, raiz): #Mayor del SubArbol Izquierdo
        if raiz.getDerecha() is not None:
            padre= raiz
            return self.maxIzquierda(raiz.getDerecha(), padre)
        else:
            return raiz, padre

    def Suprimir(self, padre, raiz):
        if raiz.getDerecha() is None and raiz.getIzquierda() is None: #Es decir, si es hoja
            if padre.getIzquierda() == raiz:
                padre.setIzquierda(None)
            if padre.getDerecha() == raiz:
                padre.setDerecha(None)
        else:
            if (raiz.getIzquierda() and raiz.getDerecha() is None) or (raiz.getIzquierda() is None and raiz.getDerecha()):
                if padre.getDerecha() == raiz:
                    if raiz.getDerecha() is not None: #Is not None
                        padre.setDerecha(raiz.getDerecha())
                    else:
                        padre.setDerecha(raiz.getIzquierda())
                if padre.getIzquierda() == raiz:
                    if raiz.getIzquierda() is not None: #Is not None
                        padre.setIzquierda(raiz.getIzquierda())
                    else:
                        padre.setIzquierda(raiz.getDerecha())
            else:
                reemplazo, oPadre= self.maxIzquierda(raiz.getIzquierda(), raiz)
                raiz.setClave(reemplazo.getClave())
                self.Suprimir(oPadre, reemplazo)



    def Buscar(self, clave, raiz):
        if raiz is not None:
            if raiz.getClave() == clave:
                return raiz
            else:
                if clave < raiz.getClave():
                    return self.Buscar(clave, raiz.getIzquierda())
                elif clave > raiz.getClave():
                    return self.Buscar(clave, raiz.getDerecha())
        else:
            print("-----------")

    def BuscarPadre(self, clave, raiz, padre):
        if raiz is not None:
            if raiz.getClave() == clave:
                return padre
            else:
                if clave < raiz.getClave():
                    padre=raiz
                    return self.BuscarPadre(clave, raiz.getIzquierda(), padre)
                elif clave > raiz.getClave():
                    padre=raiz
                    return self.BuscarPadre(clave, raiz.getDerecha(), padre)
        else:
            print("-----------")



    def Nivel(self, clave, raiz, cont): #Se usa la misma función como contador
        if raiz is None:
            return None
        if clave == raiz.getClave():
            return cont+1
        if clave < raiz.getClave():
            return self.Nivel(clave, raiz.getIzquierda(),cont+1)
        if clave > raiz.getClave():
            return self.Nivel(clave, raiz.getDerecha(), cont+1)
        #return cont

    def Hoja(self, clave, raiz):
        nodo=self.Buscar(clave, raiz)
        if nodo is None:
            print("Error con el dato ingresado.")
        else:
            if nodo.getDerecha() is None and nodo.getIzquierda() is None:
                print("El dato ({}) ingresado es hoja" .format(clave))
            else:
                print("El dato ({}) ingresado no es hoja" .format(clave))



    def HijoPadre(self, claveh, clavep, raiz): #La función sirve tanto para saber si una es hijo como si es padre
        #nodoh=self.Buscar(claveh, raiz)
        nodop=self.Buscar(clavep, raiz)
        rta=False
        if nodop is None:
            rta="Error con el dato ingresado."
        else:
            if nodop.getIzquierda() is not None:
                if nodop.getIzquierda().getClave() == claveh:
                    rta=True
            if nodop.getDerecha() is not None:
                if nodop.getDerecha().getClave() == claveh:
                    rta=True
        return rta


    def Altura(self, raiz):
        if raiz == None:
            return 0
        else:
            return 1 + max(self.Altura(raiz.getIzquierda()), self.Altura(raiz.getDerecha()))



    def Camino(self, clave, raiz, camino):
        if raiz is not None:
            if raiz.getClave() == clave:
                return camino
            else:
                if clave > raiz.getClave():
                    camino+= f"{raiz.getClave()} "
                    return self.Camino(clave, raiz.getDerecha(), camino)
                elif clave < raiz.getClave():
                    camino+= f"{raiz.getClave()} "
                    return self.Camino(clave, raiz.getIzquierda(), camino)

        else:
            print("Error con el dato ingresado.")

    def Preorden(self, raiz):
        if raiz is not None:
            print(raiz.getClave(), end="- ")
            self.Preorden(raiz.getIzquierda())
            self.Preorden(raiz.getDerecha())

    def Inorden(self, raiz):
        if raiz is not None:
            self.Inorden(raiz.getIzquierda())
            print(raiz.getClave(), end="- ")
            self.Inorden(raiz.getDerecha())

    def Postorden(self, raiz):
        if raiz is not None:
            self.Postorden(raiz.getIzquierda())
            self.Postorden(raiz.getDerecha())
            print(raiz.getClave(), end="- ")

