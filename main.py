import os
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
    1.  Cargar archivo de entrada
    2.  Gráfica
    5.  Salir
    """)
    opcion = int(input("\n Ingrese el numero de la opcion y presione enter: "))

    match opcion:

        # Caraga de archivos a memoria
        case 1:
            pass

        case 2:
           pass

            
        case 5:
            break
                
