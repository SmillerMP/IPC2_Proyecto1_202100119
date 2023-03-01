import os
from creacionTablero import *
from carga import *
from nodo import *

listaCelulas = lista()

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
    1.  Elegir Tama;o del tablero
    2.  Gráfica
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

            tablero(columnas, filas)

           

        case 2:

            cargaArchivo()
            
            listaCelulas.recorrer()
            pintarTablero(3, 4, 5)

            input()
            pass

            
        case 5:
            break

                
