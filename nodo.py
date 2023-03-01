from creacionTablero import pintarTablero
from clasesDatos import *

class nodo():

    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


class lista():
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def vacio(self):
        return self.primero == None
    

    def agregar(self, dato):
        if self.vacio() == True:
            self.primero = self.ultimo = nodo(dato)

        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)

    
    def recorrer(self):
        aux = self.primero
        while aux != None:
            print("Fila:", aux.dato.fila_CelulaViva, "Columna:",aux.dato.columna_CelulaViva, "Codigo:",aux.dato.codigo_CelulaViva)
            print("hola")
            aux = aux.siguiente



    def pintar(self):
        aux = self.primero
        while aux != None:
            #print(aux.dato.fila_CelulaViva, aux.dato.columna_CelulaViva, aux.dato.codigo_CelulaViva)
            pintarTablero(aux.dato.fila_CelulaViva, aux.dato.columna_CelulaViva, aux.dato.codigo_CelulaViva)
            aux = aux.siguiente





    
# class lista_CelulasVivas():

#     def __init__(self):
#         self.primero = None
#         self.ultimo = None
#         self.size = 0


#     def vacio(self):
#         return self.primero == None
  

#     def agregarUltimo(self, dato):
#         if self.vacio() == True:
#             self.primero = self.ultimo = nodo(dato)

#         else:
#             aux = self.ultimo
#             self.ultimo = aux.siguiente = nodo(dato)
#             self.ultimo.anterior = aux
        
#         self.size += 1


#     def agregarInicio(self,dato):
#         if self.vacio():
#             self.primero = self.ultimo = nodo(dato)
        
#         else:
#             aux = nodo(dato)
#             aux.siguiente = self.primero
#             self.primero.anterior = self.primero = aux


#         self.size += 1


#     def recorridoInicio(self):
#         aux = self.primero
        
#         while aux != None:
#             print(aux.dato.datosceldasvivas())
#             aux = aux.siguiente



#     def recorridoFinal(self):
#         aux = self.ultimo

#         while aux != None:
#             print(aux.dato)
#             aux = aux.anterior


#     def eliminarPrimero(self):
#         if self.vacio() == True:
#             print("Esta Vacio")

#         elif self.primero.siguiente == None:
#             self.primero = None
#             self.ultimo = None

#         else: 
#             self.primero = self.primero.siguiente
#             self.primero.anterior = None
#             self.size -= 1

    
#     def elilminarUltimo(self):
#         if self.vacio() == True:
#             print("Esta Vacio")

#         elif self.primero.siguiente == None:
#             self.primero = None
#             self.ultimo = None
#             self.size = 0

#         else:
#             self.utlimo = self.ultimo.anterior
#             self.ultimo.siguiente = None
#             self.size -= 1
            

#     def Size(self):
#         return self.size
    


