

class celulasVivas():

    def __init__(self, fila_CelulaViva, columna_CelulaViva, codigo_CelulaViva):
        self.fila_CelulaViva = fila_CelulaViva
        self.columna_CelulaViva = columna_CelulaViva
        self.codigo_CelulaViva = codigo_CelulaViva


    def get_fila_CelulaViva(self):
        return self.fila_CelulaViva

    def get_columna_CelulaViva(self):
        return self.columna_CelulaViva
    
    def get_codigo_CelulaViva(self):
        return self.codigo_CelulaViva


class muestra():

    def __init__(self, codiga_Muestra, descripcion_Muestra, filas_Muestra, columunas_Muestra):
        self.codiga_Muestra = codiga_Muestra
        self.descripcion_Muestra = descripcion_Muestra
        self.filas_Muestra = filas_Muestra
        self.columunas_Muestra = columunas_Muestra


class organismos():

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    