import os
from creacionTablero import *
from nodo import *
from carga import *

listaCelulas = lista()
listaCelulas2 = lista()

print("""
╔═════════════════════════════════════════════════╗
║                   BIENVENIDO...                 ║                                                
╚═════════════════════════════════════════════════╝

Presione enter para continuar...
""")
input()

opcion = 0

# Repetite esto hasta que encuentre un brake
while opcion != 5:
    #Limpiar la pantalla
    os.system ("cls") 
    submenu = 0

    print("------------------   MENU   ------------------\n\n")
    print("""
    1.  Elegir Tamaño del tablero
    2.  Graficar Tablero
    5.  Salir
    """)
    opcion = int(input("\n Ingrese el numero de la opcion y presione enter: "))

    match opcion:

        case 1:
            os.system ("cls") 
            print("------------------   TABLERO   ------------------\n\n")

            print("Recuerda que el maximo de columnas y filas es de 10 mil\n")

            columnas = int(input("Cuantas Columnas desea: "))
            filas = int(input("Cuantas Filas desea: "))

            while True:

                if columnas > 10000 or filas > 10000:
                    print("Las filas y/o columnas no pueden ser mayor de 10000, vuelve a ingresar los datos \n")
                    columnas = int(input("Cuantas Columnas desea: "))
                    filas = int(input("Cuantas Filas desea: "))
                
                else:
                    break
            

            tablero(columnas, filas)

           

        case 2:

            cargaArchivo()
            listaCelulas = get_listaCelulas()
            listaCelulas.tablero()
            crearPdf()

            #listaCelulas.experimento(fila_experimento, columna_experimento, codigo_experimento)
            #pintarTablero(3, 4, 5)


            
        case 5:
            print("Gracias Por usar el programa :D")
            break

                
