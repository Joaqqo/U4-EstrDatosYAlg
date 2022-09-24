from ArbolBinarioBusqueda import ABB

if __name__ == '__main__':
    arbol=ABB(70)
    raiz=arbol.getRaiz()
    arbol.Insertar(47, raiz)
    arbol.Insertar(92, raiz)
    arbol.Insertar(35, raiz)
    arbol.Insertar(68, raiz)
    arbol.Insertar(83, raiz)
    arbol.Insertar(100, raiz)
    arbol.Preorden(raiz)
    print("---")
    arbol.Frontera(raiz)
    print("---")
