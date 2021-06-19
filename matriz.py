from cabezera import cabezera
from nodo_matriz import  nodo_matriz
class matriz():
    def __init__(self):
        self.cabecera = cabezera(0, 0)
        self.cabezaNodo = None
    def buscar_x(self, X):
        print('insertar x')
        node = self.cabecera
        while node is not None:
            print(node.fil_x)
            if(node.fil_x == X):
                print('')
#                return node
            node = node.siguiente
#        return None
    def buscar_y(self,y):
        print('insertar y')
        node = self.cabecera
        while node is not None:
            print(node.fil_y)
            if(node.fil_y == y):
                print('')
#                return node
            node = node.siguiente
#        return None

    def insertar_y_x(self,nuevoX,nuevoY,cabeza):
        node = self.cabecera
        if self.cabecera.siguiente is None:
            node.siguiente = cabezera(nuevoX,nuevoY)
            print

    def insertar_nodo_cont(self,posx,posy,nuevo):
        print("insertar Color")