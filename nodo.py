class nodo():

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None



        
class listaDobleEnlazada():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0


    def vacio(self):
        return self.primero == None
  

    def agregarUltimo(self, dato):
        if self.vacio() == True:
            self.primero = nodo(dato)
            self.ultimo = nodo(dato)

        else:
            aux = self.ultimo
            self.ultimo = nodo(dato)
            aux.siguiente = nodo(dato)
            self.ultimo.anterior = aux
        
        self.size += 1


    def agregarInicio(self,dato):
        if self.vacio():
            self.primero = nodo(dato)
            self.ultimo = nodo(dato)
        
        else:
            aux = nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux


    def recorridoInicio(self):
        aux = self.primero
        
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente


    def recorridoFinal(self):
        aux = self.ultimo

        while aux != None:
            print(aux.dato)
            aux = aux.anterior


    def eliminarPrimero(self):
        if self.vacio() == True:
            print("Esta Vacio")

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None

        else: 
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1

    
    def elilminarUltimo(self):
        if self.vacio() == True:
            print("Esta Vacio")

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
            self.size = 0

        else:
            self.utlimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
            

    def size(self):
        return self.size