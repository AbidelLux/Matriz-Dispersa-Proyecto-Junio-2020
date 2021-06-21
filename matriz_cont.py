
class matriz_cont():
    def __init__(self)-> None:
        self.head = None
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None
    def insertarx(self,posx,posy,listaCabeza,nuevoNodo):
        listax = listaCabeza.cabX
        while listax is not None:
            if(listax.fil_x == posx):
                listax.abajo = nuevoNodo
                nuevoNodo.arriba = listax
                return listax
            listax=listax.siguiente

    def insertary(self, posx, posy, listaCabeza, nuevoNodo):
        listay = listaCabeza.cabY
        while listay is not None:
            if(listay.fil_y == posy):
                listay.siguiente = nuevoNodo
                nuevoNodo.anterior = listay
                return listay
            listay = listay.abajo
    def mostrar(self,posx,listaCabeza):
        listax = listaCabeza.cabX
        while listax is not None:
            if (listax.fil_x == posx):
                print('nodo.abajo de',listax.fil_x)
                print(listax.abajo.cont)
                return listax
            listax = listax.siguiente
    def mostra(self,posy,listaCabeza):
        listay = listaCabeza.cabY
        while listay is not None:
            if (listay.fil_y == posy):
                print('nodo.siguiente de',listay.fil_y)
                print(listay.siguiente.cont)
                return listay
            listay = listay.abajo