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
    funciones_matriz.ordenar_cab_fila(y)
    funciones_matriz.ordenar_cab_columna(x)
    print('***************************')

    funciones_matriz.insertar_x_final(4)
    funciones_matriz.insertar_y_final(4)
    print('*****************************')
    funciones_matriz.insertar_x_final(8)
    funciones_matriz.insertar_x_antes(3,4)
    funciones_matriz.insertar_x_antes(6,8)
    funciones_matriz.insertar_x_final(10)
    print('*******************************')

    funciones_matriz.insertar_y_final(8)
    funciones_matriz.insertar_y_antes(3,4)
    funciones_matriz.insertar_y_antes(6,8)
    funciones_matriz.insertar_y_final(10)
   # funciones_matriz.ordenar_cab_fila(int(5))
    #funciones_matriz.ordenar_cab_fila(int(8))
    print('*******************************')
    #func_matriz_cont.insertarx(x,y,funciones_matriz,nodo_matriz(cont,x,y))
    #func_matriz_cont.insertary(x,y,funciones_matriz,nodo_matriz(cont,x,y))
    #func_matriz_cont.mostrar(x,funciones_matriz)

    #func_matriz_cont.mostra(y,funciones_matriz)
    funciones_matriz.buscar_y(y)
    funciones_matriz.buscar_x(x)
    #funciones_matriz.buscar_x(x)
    print("********************************")
    print("probar insertar antes de 2 un 1 en columnas")
    funciones_matriz.ordenar_cab_fila(1)
    print("probar inserta despues de 10 un 11 en columnas")
    funciones_matriz.ordenar_cab_fila(11)
    print("inserta antes de 6")
    funciones_matriz.ordenar_cab_fila(5)
    print("inserar antes de 10")
    funciones_matriz.ordenar_cab_fila(9)
    print("*******************************")
    funciones_matriz.buscar_y(1)
