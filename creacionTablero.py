import os

def tablero(columnas, filas):

    # Ruta del archivo de graphviz
    tablero_dot = open("tablero.dot", "w")
    tablero_dot.write('graph { \n')
    tablero_dot.write('rankdir = TB \n' )
    tablero_dot.write('node[shape=record, fontname="Arial", fontsize=15] \n')


    for x in range(columnas):
        
        for y in range(filas-1):
            tablero_dot.write("celda" + str(y) + str(x) + " -- " + "celda" + str(y+1) + str(x) + "\n")
    
        tablero_dot.write("\n")



    tablero_dot.write("/*------------ Encuadre ------------*/\n")
    for y in range(filas):
        tablero_dot.write("{rank = same")
        for x in range(columnas):
            tablero_dot.write("; celda" + str(y) + str(x))

        tablero_dot.write("} \n")
    
        



    tablero_dot.write("} \n")
    tablero_dot.close()