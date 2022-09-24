from ArbolBinarioBusqueda import ABB

import os

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n BIENVENIDO')
        print('\n----------------Opciones----------------')
        print('\n 1-Nodo padre y nodo hermano')
        print('\n 2-Cantidad de nodos')
        print('\n 3-Altura del árbol')
        print('\n 4-Sucesores del nodo ingresado')
        print('\n 5-Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            clave=int(input("Ingrese el nodo que desea buscar: "))
            while arbol.getRaiz().getClave() == clave: #En caso de que ingresen la raíz
                clave=int(input("El nodo ingresado es la raíz, no tiene hermanos ni padres, ingrese otro nodo:  "))
            nodo= arbol.Buscar(clave,raiz)
            if nodo is None: #Si hay un error en la búsqueda
                print("Error con el nodo ingresado.")
            else: #En el caso de que no haya error en la búsqueda
                padre=arbol.BuscarPadre(nodo.getClave(), raiz, None) #Busca al padre
                if padre.getIzquierda() is None or padre.getDerecha() is None: #En el caso de que el nodo ingresado no tenga hermano
                    print("El nodo padre del nodo ingresado es: {}." .format(padre.getClave()))
                    print("El nodo ingresado no tiene hermano.")
                else: #En el caso de que si tenga hermano
                    if padre.getIzquierda().getClave() == clave:
                        print("El nodo padre del nodo ingresado es: {}." .format(padre.getClave()))
                        print("El nodo hermano del nodo ingresado es: {}." .format(padre.getDerecha().getClave()))
                    elif padre.getDerecha().getClave() == clave:
                        print("El nodo padre del nodo ingresado es: {}." .format(padre.getClave()))
                        print("El nodo hermano del nodo ingresado es: {}." .format(padre.getIzquierda().getClave()))
        if(opcion == 2):
            cuenta=arbol.Cuenta(raiz)
            print("La cantidad de nodos del árbol es: {}".format(cuenta))
        if(opcion == 3):
            print("La altura del árbol es: {}" .format(arbol.Altura(raiz)))
        if(opcion == 4):
            clave=int(input("Ingrese el nodo que desea ver los sucesores:  "))
            nodo= arbol.Buscar(clave, raiz)
            if nodo is None:
                print("Error con el nodo ingresado.")
            else:
                arbol.Sucesores(nodo)
        if(opcion == 5):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')


if __name__ == '__main__':
    arbol=ABB(70)
    raiz=arbol.getRaiz()
    arbol.Insertar(47, raiz)
    arbol.Insertar(92, raiz)
    arbol.Insertar(35, raiz)
    arbol.Insertar(68, raiz)
    arbol.Insertar(83, raiz)
    arbol.Insertar(100, raiz)
    arbol.Insertar(79, raiz)
    menu()
