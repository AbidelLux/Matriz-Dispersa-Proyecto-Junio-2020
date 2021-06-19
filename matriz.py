from cabezera import cabezera
from nodo_matriz import  nodo_matriz
class matriz():
    def __init__(self):
        self.cabecera = cabezera(0, 0)
        self.cabezaNodo = None
    def insertar_x(self, X):
        print('insertar x')
        node = self.cabecera
        while node is not None:
            print(node.fil_x)
            if(node.fil_x == X):
                return node
            node = node.siguiente
        return None
    def insertar_y(self,y):
        print('insertar y')
        node = self.cabecera
        while node is not None:
            print(node.fil_y)
            if(node.fil_y == y):
                return node
            node = node.siguiente
        return None

    def insertar_nodo_cont(self):
        print("insertar Color")