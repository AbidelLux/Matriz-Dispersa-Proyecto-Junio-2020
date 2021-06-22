class nodo_matriz():
    def __init__(self,color,columna,fila):
        #punteros de nodo
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None
        self.cont = color
        self.columna = columna
        self.fila = fila
