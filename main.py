# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matriz import matriz


if __name__ == '__main__':
    funciones_matriz = matriz()
    x = int(input('Ingresar posicion x :'))
    y = int(input('Ingresar posicion y :'))
    funciones_matriz.insertar_y_x(x,y,funciones_matriz)
    funciones_matriz.buscar_y(y)
    funciones_matriz.buscar_x(x)
