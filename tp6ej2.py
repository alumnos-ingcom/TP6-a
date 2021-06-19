################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def anagrama(arg1, arg2):
    
    cadena1 = list(arg1.lower()) #creo una cadena en mayusculas del arg1
    cadena2 = list(arg2.lower()) #creo una cadena en mayusculas del arg2
    
    limpiar(cadena1)     #limpio ambas cadenas
    limpiar(cadena2)     
    
    if len(cadena1) != len(cadena2):   #deben tener igual cantidad de letras
        return False
    
    for letra in cadena1:
        if letra in cadena2:
            cadena2.remove(letra)
        else:
            return False
    return True
        
        

def limpiar(palabra):    
    
    #eliminar espacios
    while " " in palabra:
        palabra.remove(" ")
    
    #eliminar comas
    while "," in palabra:
        palabra.remove(",")
    
    #eliminar acentos
    for i, letra in enumerate(palabra):            
        
        if   letra == "á": palabra[i] = "a"
        elif letra == "é": palabra[i] = "e"        
        elif letra == "í": palabra[i] = "i"        
        elif letra == "ó": palabra[i] = "o"        
        elif letra == "ú": palabra[i] = "u"
    
    salida = "".join(palabra)
    return salida



def principal():
    
    archivo = open("anagramas.txt", "r", encoding="utf-8") #guardo el documento en 'archivo'

    lineas = archivo.read().splitlines() #creo una lista donde cada elemento es una linea del archivo

    for i,e in enumerate(lineas):
        
        palabras = lineas[i].split("–") #esto almacena lista de dos palabras de cada linea       
        
        if len(palabras) == 2:
            print(f"{i+1} {e} ({anagrama(palabras[0], palabras[1])})")
    
    archivo.close()

if __name__ == "__main__":
    principal()

