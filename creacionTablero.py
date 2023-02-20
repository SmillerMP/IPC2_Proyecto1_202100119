import os

def tablero(columnas, filas):

    # Ruta del archivo de graphviz
    tablero_dot = open("tablero.dot", "w")
    tablero_dot.write('graph { \n')
    tablero_dot.write('rankdir = TB \n' )
    tablero_dot.write('node[shape= rect, fontname = "Arial", fontsize = 14] \n')

    # Crea las conexiones de manera verticasl
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

    # Encuadre de los nodos
    tablero_dot.write("/*------------ Encuadre ------------*/\n")
    for y in range(filas):
        tablero_dot.write("{rank = same")
        for x in range(columnas):
            tablero_dot.write("; F" + str(y) + "C" + str(x))

        tablero_dot.write("} \n")
    
        



    tablero_dot.write("} \n")
    tablero_dot.close()