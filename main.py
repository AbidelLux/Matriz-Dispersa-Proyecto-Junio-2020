# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matriz import matriz
from matriz_cont import matriz_cont
from nodo_matriz import nodo_matriz

if __name__ == '__main__':
    funciones_matriz = matriz()
    func_matriz_cont = matriz_cont()
    x = int(input('Ingresar posicion x :'))
    y = int(input('Ingresar posicion y :'))
    cont = input('Ingresar color: ')
    funciones_matriz.insertar_x(x)
    funciones_matriz.insertar_y(y)
    func_matriz_cont.insertarx(x,y,funciones_matriz,nodo_matriz(cont))
    func_matriz_cont.insertary(x,y,funciones_matriz,nodo_matriz(cont))
    func_matriz_cont.mostrar(x,funciones_matriz)
    func_matriz_cont.mostra(y,funciones_matriz)
    funciones_matriz.buscar_y(y)
    funciones_matriz.buscar_x(x)
