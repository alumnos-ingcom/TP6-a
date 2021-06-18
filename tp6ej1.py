################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def anagrama(arg1, arg2):
    
    cadena1 = list(arg1.lower()) #creo una cadena en minúsculas del arg1
    cadena2 = list(arg2.lower()) #creo una cadena en minúsculas del arg2
    
    limpiar(cadena1)     #quito los acentos y espacios en cadena1
    limpiar(cadena2)     #quito los acentos y espacios en cadena2
    
    if len(cadena1) != len(cadena2):
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
    
    #eliminar acentos
    for i, letra in enumerate(palabra):            
        
        if   letra == "á": palabra[i] = "a"
        elif letra == "é": palabra[i] = "e"        
        elif letra == "í": palabra[i] = "i"        
        elif letra == "ó": palabra[i] = "o"        
        elif letra == "ú": palabra[i] = "u"
    
    salida = "".join(palabra)
    return salida


    
if __name__ == "__main__":
    test1 = input("Ingrese primer texto: ")
    test2 = input("Ingrese segundo texto: ")
    print(anagrama(test1,test2))
