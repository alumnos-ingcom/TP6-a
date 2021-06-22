################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################



def cifrar_archivo(arg="texto de ejemplo", ext="txt", rot=13):
    
    try:
        nombre = f"{arg}.{ext}"
        archivo = open(nombre)
    except FileNotFoundError:
        return "El archivo no existe"
    
    lista = list("abcdefghijklmnñopqrstuvwxyz") #creo lista de letras sobre la cual se usará el rot
    
    salida = [] #preparo una nueva lista en la que se guardará el cifrado
  

    for i,letra in enumerate(archivo.read()): #para cada caracter ingresado como argumento
        
        
        if letra.isalpha(): #solo funciona con letras
            
            if letra.isupper(): #si está en mayusculas:               
                letra_min = letra.lower() #la convierto en minuscula                          
                indice = lista.index(letra_min) +rot #obtengo el indice con la nueva posicion segun rot           
                salida.append(lista[indice % len(lista)].upper()) #le añado la nueva letra a salida, volviendo a mayusc
                
            
            else:                                     
                indice = lista.index(letra) +rot #obtengo el indice con la nueva posicion segun rot                         
                salida.append(lista[indice % len(lista)]) #le añado la nueva letra a salida
                        
            continue
        
        salida.append(letra) #añade a la salida el mismo caracter sin modificar, ya que no es una letra
      
    resultado = "".join(salida) #junta la lista de salida como una cadena
    
    archivo_nuevo = open(f"{arg}.cesar.txt", "w")
    archivo_nuevo.write(resultado)
    
    archivo.close(), archivo_nuevo.close()
    return "Archivo cifrado con éxito"


if __name__ == "__main__":
    
    print(cifrar_archivo())


