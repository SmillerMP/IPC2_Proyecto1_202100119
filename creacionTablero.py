import os

codigos_asignados = {}
colores_disponibles = ['red', 'green', 'blue', 'yellow', 'orange', 'brown', 'blac', 'pink', 'chartreuse', 'darkorchid1', 'deepskyblue', 'gold3', 'gold1', 'firebrick1', 'blueviolet', 'aquamarine']

def asignar_color(codigo):
    if codigo in codigos_asignados:
        return codigos_asignados[codigo]
    color = colores_disponibles.pop(0)
    codigos_asignados[codigo] = color
    return color

def pintarTablero(fila, columna, codigo):

    nombreNodo = "F" + str(fila) + "C" + str(columna)
    color = None
    
    # Lee el archivo y cuenta cuantas lineas tiene el archivo 
    tablero_dot = open("tablero.dot", "r")
    archivoDot = tablero_dot.readlines()

    numeroLineas = len(archivoDot)

    # Incerta en la lista archivoDot las nuevas lineas en una posicion antes de cerrar el archivo
    lineasNuevas= [nombreNodo + '[color =' + asignar_color(codigo) + ', style = filled]\n']
    #lineasNuevas = ["hola\n", "samuel\n"]
    archivoDot.insert(numeroLineas - 2, ''.join(lineasNuevas))

    tablero_dot = open("tablero.dot", "w")
    tablero_dot.writelines(archivoDot)




def tableroDinamico(filaMax, columnaMax):
    # Ruta del archivo de graphviz
    tablero_dot = open("tablero.dot", "w")
    tablero_dot.write('graph { \n')
    tablero_dot.write('rankdir = TB \n' )
    tablero_dot.write('node[shape= rect, fontname = "Arial", fontsize = 14] \n')

    # Crea las conexiones de manera vertical
    for x in range(1, columnaMax+2):
        for y in range(1,filaMax+1):
            tablero_dot.write("F" + str(y) + "C" + str(x) + " -- " + "F" + str(y+1) + "C" + str(x) + "\n")
    
        tablero_dot.write("\n")


    tablero_dot.write("/*------------ Encuadre ------------*/\n")
    for y in range(1,filaMax+2):
        tablero_dot.write("{rank = same")
        for x in range(1,columnaMax+2):
            tablero_dot.write("; F" + str(y) + "C" + str(x))

        tablero_dot.write("} \n")
    

    tablero_dot.write("\n\n")     

    tablero_dot.write("}")
    tablero_dot.close()






def tablero(columnas, filas):

    # Ruta del archivo de graphviz
    tablero_dot = open("tablero.dot", "w")
    tablero_dot.write('graph { \n')
    tablero_dot.write('rankdir = TB \n' )
    tablero_dot.write('node[shape= rect, fontname = "Arial", fontsize = 14] \n')


    # Recordar que en el sistema de cordenadas F representa las filas y C las columnas

    # Crea las conexiones de manera vertical
    for x in range(1, columnas+1):
        for y in range(1,filas):
            tablero_dot.write("F" + str(y) + "C" + str(x) + " -- " + "F" + str(y+1) + "C" + str(x) + "\n")
    
        tablero_dot.write("\n")


    # Crea las conexiones de manera horizontals
    # tablero_dot.write("\n\n/*------------ Conexiones Horizontales ------------*/\n")

    # for y in range(1, filas+1):
    #     for x in range(1,columnas):
    #         tablero_dot.write("F" + str(y) + "C" + str(x) + " -- " + "F" + str(y) + "C" + str(x+1) + "\n")
        
    #     tablero_dot.write("\n")


    # tablero_dot.write("\n\n")


    # Encuadre de los nodos, el encuadre sirve para que las filas esten alineadas de manera horizontal
    # de esta manera se le da una apariencia de matriz al grafo
    tablero_dot.write("/*------------ Encuadre ------------*/\n")
    for y in range(1,filas+1):
        tablero_dot.write("{rank = same")
        for x in range(1,columnas+1):
            tablero_dot.write("; F" + str(y) + "C" + str(x))

        tablero_dot.write("} \n")
    

    tablero_dot.write("\n\n")     



    tablero_dot.write("}")
    tablero_dot.close()
    crearPdf()


def crearPdf():
    os.system("dot.exe -Tpdf tablero.dot -o  tablero.pdf")
    

