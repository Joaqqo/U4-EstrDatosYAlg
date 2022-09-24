from ArbolBinarioBusqueda import ABB

if __name__ == '__main__':
    arbol=ABB(70)
    #arbol.InsertarRaiz(70)
    raiz=arbol.getRaiz()
    arbol.Insertar(47, raiz)
    arbol.Insertar(92, raiz)
    arbol.Insertar(35, raiz)
    arbol.Insertar(68, raiz)
    arbol.Insertar(83, raiz)
    arbol.Insertar(100, raiz)
    arbol.Insertar(79, raiz)
    arbol.Preorden(raiz)
    print("---")
    arbol.Inorden(raiz)
    print("---")
    arbol.Postorden(raiz)
    print("---")

    nodo= arbol.Buscar(8, raiz)
    if nodo is None:
        print("Error con el dato ingresado.")
    else:
        print(nodo)
        print(nodo.getClave())

    print("----------------------------")
    nivel=arbol.Nivel(100, raiz,0)
    print("El nivel de 100 es: {}" .format(nivel)) #Debería traer nivel 3
    print("----------------------------")
    arbol.Hoja(70,raiz) #Al ser la raíz, no es hoja.
    print("----------------------------")
    altura=arbol.Altura(raiz)
    print("La altura del árbol es de: {}" .format(altura))
    print("----------------------------")
    rta=arbol.HijoPadre(79, 83, raiz)#La función sirve tanto como para saber si una clave es hijo o padre de otra.
    if rta:
        print("La clave 79 es hijo de 83")
        print("La clave 83 es padre de 79")
    else:
        print("La clave 79 no es hijo de 83")
        print("La clave 83 no es hijo de 79")
    print("----------------------------")

    total=arbol.Camino(68, raiz,"")
    print("El camino de 68 es: {}" .format(total))


    print("-----------------------------------------------")
    nodo=arbol.Buscar(100, raiz)
    if nodo is None:
        print("Error con el dato ingresado.")
    else:
        padre= arbol.BuscarPadre(100, raiz, None)
        arbol.Suprimir(padre, nodo)

    nodo=arbol.Buscar(100, raiz) #No lo encuentra porque se suprimió antes.
    if nodo is None:
        print("Error con el dato ingresado.")




