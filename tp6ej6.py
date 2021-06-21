################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def hace_etiqueta(contenido, etiqueta):
    return '<%s>%s</%s>' % (etiqueta, contenido, etiqueta)

def hace_comenta(contenido):
    
    return '<!-- %s -->' % (contenido)
def crear_pagina(nombre, pagina):
    barra = chr(92)
    nombre = barra + nombre + '.html'
    ruta = 'D:\Datos De Usuario\Desktop'
    ruta = (ruta + nombre)
    nuevoarchivo = open(ruta, "w") 
    nuevoarchivo.write(pagina)

def principal():
    
    
    encabezado = hace_etiqueta('Hola HTML', 'h1') + '\n'
    parrafo = encabezado + hace_etiqueta('Esto es un párrafo', 'p') 
    comenta = hace_comenta('comentario html')
    print(comenta)
    parrafo2 = hace_etiqueta('\n'+parrafo+'\n', 'body')
    parrafo3 = hace_etiqueta('\n'+parrafo2+'\n', 'html')
    print(parrafo3)
    
    nombre = input("¿Como desea nombrar su archivo?: ")
    crear_pagina(nombre, parrafo3)   
    

if __name__ == "__main__":
    principal()     