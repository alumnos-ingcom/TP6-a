################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def copiadora(ruta, ruta2):
    #abro el archivo de la ruta indicada#
    archivo = open(ruta, "r")
    #guardo el contenido en una variable#
    contenido = archivo.read()
    #leo el contenido de la variable y lo guardo en una nueva variable#
    nuevoarchivo = open(ruta2, "w")
    #creo el nuevo archivo en la ruta que se indico#
    nuevoarchivo.write(contenido)
    #escribo el archivo con el contenido que guarde previamente de el primer archivo que lei#
    return


def principal():
    ruta = input(str("Ingrese la ruta del archivo que quiere copiar: "))
    ruta2 = input(str("Ingrese la ruta de destino del nuevo archivo: "))
    copiadora(ruta, ruta2)
    
if __name__ == "__main__":
    principal()