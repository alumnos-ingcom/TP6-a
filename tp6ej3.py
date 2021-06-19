################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def copiadora(ruta, ruta2):
    
    archivo = open(ruta, "r")
    
    contenido = archivo.read()
    
    nuevoarchivo = open(ruta2, "w")
    
    nuevoarchivo.write(contenido)
    
    return


def prueba():
    ruta = input(str("Ingrese la ruta del archivo que quiere copiar: "))
    ruta2 = input(str("Ingrese la ruta de destino del nuevo archivo: "))
    copiadora(ruta, ruta2)
    
if __name__ == "__main__":
    prueba()