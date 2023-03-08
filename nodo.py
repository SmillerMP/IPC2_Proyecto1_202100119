from creacionTablero import *
from clasesDatos import *




class nodo():

    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


# Clase temporal
class listaExperimento():
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

    def eliminar_todo(self):
        aux = self.primero
        while aux != None:
            siguiente_nodo = aux.siguiente
            del aux
            aux = siguiente_nodo
        self.primero = self.ultimo = None





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
            aux = aux.siguiente



    def actualizar_valores(self, lista_auxiliar):
            aux_principal = self.primero
            while aux_principal != None:
                aux_auxiliar = lista_auxiliar.primero
                while aux_auxiliar != None:
                    if aux_principal.dato.fila_CelulaViva == aux_auxiliar.dato.fila_CelulaViva and aux_principal.dato.columna_CelulaViva == aux_auxiliar.dato.columna_CelulaViva:
                        aux_principal.dato = aux_auxiliar.dato
                    aux_auxiliar = aux_auxiliar.siguiente
                aux_principal = aux_principal.siguiente



    def tablero(self):
        filaMax = 0
        columnaMax = 0
        aux = self.primero
        while aux != None:

            aux.dato.fila_CelulaViva = int(aux.dato.fila_CelulaViva)
            aux.dato.columna_CelulaViva = int(aux.dato.columna_CelulaViva)

            if filaMax < aux.dato.fila_CelulaViva:
                filaMax = aux.dato.fila_CelulaViva

            if columnaMax < aux.dato.columna_CelulaViva:
                columnaMax = aux.dato.columna_CelulaViva

            aux = aux.siguiente
        
        tableroDinamico(filaMax, columnaMax)

        aux = self.primero
        while aux != None:
            pintarTablero(aux.dato.fila_CelulaViva, aux.dato.columna_CelulaViva, aux.dato.codigo_CelulaViva)
            aux = aux.siguiente



    # def experimento(self, fila, columna, codigo):
    #     listaTemporal = []

    #     aux = self.primero
    #     while aux != None:
    #         aux.dato.fila_CelulaViva = int(aux.dato.fila_CelulaViva)
    #         aux.dato.columna_CelulaViva = int(aux.dato.columna_CelulaViva)

    #         if (fila == aux.dato.fila_CelulaViva) and (columna < aux.dato.columna_CelulaViva) and (codigo == aux.dato.codigo_CelulaViva):

    #             contador = 0
    #             vivo = self.primero
    #             while vivo != None:
    #                 vivo.dato.fila_CelulaViva = int(vivo.dato.fila_CelulaViva)
    #                 vivo.dato.columna_CelulaViva = int(vivo.dato.columna_CelulaViva)

    #                 if  (vivo.dato.fila_CelulaViva == columna) and (vivo.dato.columna_CelulaViva > columna) and (vivo.dato.columna_CelulaViva < aux.dato.columna_CelulaViva):
    #                     contador += 1
    #                     print(contador)
                        
                        
    #                 vivo = vivo.siguiente 

    #             if contador == ((aux.dato.columna_CelulaViva - columna)-1):
    #                 pass
                    
                

    #         aux = aux.siguiente


