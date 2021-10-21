class Matriz:
    
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        vector = []

        for i in range(filas):
            for j in range(columnas):
                vector.append(0)
            self.matriz.append(vector)
            vector = []


    def actualizar(self, filas, columnas):
        self.__init__(filas, columnas)


    def mostrar(self):

        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.matriz[i][j], end=" ")
            print("\n")


    def getFilas(self):
        return self.filas

    
    def getColumnas(self):
        return self.columnas


    def getVal(self, i, j):
        return self.matriz[i][j]


    def setVal(self, i, j, val):
        self.matriz[i][j] = val