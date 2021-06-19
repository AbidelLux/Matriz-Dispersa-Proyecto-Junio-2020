# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matriz import matriz

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    funciones_matriz = matriz()
    x = int(input('Ingresar posicion x :'))
    y = int(input('Ingresar posicion y :'))
    funciones_matriz.insertar_x(x)
    funciones_matriz.insertar_y(y)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
