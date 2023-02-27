import xml.etree.ElementTree as ET
from clasesDatos import *


def cargaArchivo(self):
    ruta = input("Ingrese la ruta ABASOLUTA del arhivo: ")
    tree = ET.parse(ruta)
    root = tree.getroot()


    contador = 1

    for lista in root:
        match contador:

            case 1:
                for organismo in lista:
                    codigo = organismo.attrib["codigo"]
                    nombre = organismo.attrib["nombre"]

                    nueva_Organismo = organismos(codigo, nombre)



            case 2:
                for muestras in lista:
                    codigoMuestra = muestras.attrib["codigo"]
                    descripcionMuestra = muestras.attrib["descripcion"]
                    filasMuestra = muestras.attrib["filas"]
                    columunasMuestra = muestras.attrib["columnas"]

                    nueva_Muestra = muestra(codigoMuestra, descripcionMuestra, filasMuestra, columunasMuestra)

                    listaCelulasVivas = muestras.attrib["listadoCeldasVivas"]

                    for celdaViva in listaCelulasVivas:
                        filaCelulaViva = celdaViva.attrib["fila"]
                        columnaCelulaViva = celdaViva.attrib["columna"]
                        codigoOrganismoVivo = celdaViva.attrib["codigoOrganismo"]

                        nuevo_CelulasVivas = celulasVivas(filaCelulaViva, columnaCelulaViva, codigoOrganismoVivo)

        contador += 1







            
