from nodo_cabezeraX import nodo_cabezeraX
from nodo_cabezeraY import nodo_cabezeraY

class matriz():
    def __init__(self):
        self.cabX = nodo_cabezeraX(0)
        self.cabY= nodo_cabezeraY(0)
    def buscar_x(self, X):
        print('insertar x')
        node = self.cabX
        while node is not None:
            print(node.fil_x)
            if(node.fil_x == X):
                print('')
                return node
            node = node.siguiente
        return None
    def buscar_y(self,y):
        print('insertar y')
        node = self.cabY
        while node is not None:
            print(node.fil_y)
            if(node.fil_y == y):
                print('')
                return node
            node = node.abajo
        return None

    def insertar_x(self,nuevoX):
        node = self.cabX
        while node is not None:
            if node.siguiente is None:
                if node.anterior is None:
                    nuevo_nodo = nodo_cabezeraX(nuevoX)
                    node.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = node
                    break

    def insertar_y(self,nuevoY):
        node = self.cabY
        while node is not None:
            if node.anterior is None:
                if node.arriba is None:
                    nuevo_nodo = nodo_cabezeraY(nuevoY)
                    node.abajo = nuevo_nodo
                    nuevo_nodo.arriba = node
                    break
