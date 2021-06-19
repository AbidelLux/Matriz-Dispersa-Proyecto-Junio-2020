class nodo_matriz():
    def __init__(self,color):
        #punteros de nodo
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None
        self.cont = color