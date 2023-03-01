import xml.etree.ElementTree as ET
from clasesDatos import *
from nodo import *


listaCelulas = lista()


def get_listaCelulas():
    return listaCelulas



def cargaArchivo():
    ruta = input("Ingrese la ruta ABASOLUTA del arhivo: ")
    tree = ET.parse(ruta)
    root = tree.getroot()


    contador = 1


    for organismo in root.findall(".//organismo"):
        codigo = organismo.find("codigo").text
        nombre = organismo.find("nombre").text
        
        #print(f"Código: {codigo}, Nombre: {nombre}")


    for muestra in root.findall(".//muestra"):
        codigoMuestra = muestra.find("codigo").text
        descripcionMuestra = muestra.find("descripcion").text
        filasMuestra = muestra.find("filas").text
        columunasMuestra = muestra.find("columnas").text

        #print(f"Código: {codigoMuestra}, Descripción: {descripcionMuestra}, filas: {filasMuestra}, columnas: {columunasMuestra}")


        for celdaViva in muestra.findall("listadoCeldasVivas/celdaViva"):
            filaCelulaViva = celdaViva.find("fila").text
            columnaCelulaViva = celdaViva.find("columna").text
            codigoOrganismoVivo = celdaViva.find("codigoOrganismo").text

            #print(f"Fila: {filaCelulaViva}, Columna: {columnaCelulaViva}, Codigo: {codigoOrganismoVivo}")

            nuevas_celdaViva = celulasVivas(filaCelulaViva, columnaCelulaViva, codigoOrganismoVivo)
            listaCelulas.agregar(nuevas_celdaViva)

    

