import os


def pintarTablero(fila, columna, codigo):

    nombreNodo = "F" + str(fila-1) + "C" + str(columna-1)
    color = None
    if codigo == "organismo3":
        color = "yellow"

    elif codigo == "organismo2":
        color = "red"
    
    else:
        color = "blue"

    # Lee el archivo y cuenta cuantas lineas tiene el archivo 
    tablero_dot = open("tablero.dot", "r")
    archivoDot = tablero_dot.readlines()

    numeroLineas = len(archivoDot)

    # Incerta en la lista archivoDot las nuevas lineas en una posicion antes de cerrar el archivo
    #lineasNuevas= [nombreNodo + '[color =' + color + ', style = filled \n']
    lineasNuevas = ["hola\n", "samuel\n"]
    archivoDot.insert(numeroLineas - 2, ''.join(lineasNuevas))

    tablero_dot = open("tablero.dot", "w")
    tablero_dot.writelines(archivoDot)



def tablero(columnas, filas):

    # Ruta del archivo de graphviz
    tablero_dot = open("tablero.dot", "w")
    tablero_dot.write('graph { \n')
    tablero_dot.write('rankdir = TB \n' )
    tablero_dot.write('node[shape= rect, fontname = "Arial", fontsize = 14] \n')


    # Recordar que en el sistema de cordenadas F representa las filas y C las columnas

    # Crea las conexiones de manera vertical
    for x in range(columnas):
        for y in range(filas-1):
            tablero_dot.write("F" + str(y) + "C" + str(x) + " -- " + "F" + str(y+1) + "C" + str(x) + "\n")
    
        tablero_dot.write("\n")


    # Crea las conexiones de manera horizontal
    for y in range(filas):
        for x in range(columnas-1):
            tablero_dot.write("F" + str(y) + "C" + str(x) + " -- " + "F" + str(y) + "C" + str(x+1) + "\n")
        
        tablero_dot.write("\n")


    tablero_dot.write("\n\n")


    # Encuadre de los nodos, el encuadre sirve para que las filas esten alineadas de manera horizontal
    # de esta manera se le da una apariencia de matriz al grafo
    tablero_dot.write("/*------------ Encuadre ------------*/\n")
    for y in range(filas):
        tablero_dot.write("{rank = same")
        for x in range(columnas):
            tablero_dot.write("; F" + str(y) + "C" + str(x))

        tablero_dot.write("} \n")
    

    tablero_dot.write("\n\n")     



    tablero_dot.write("}")
    tablero_dot.close()