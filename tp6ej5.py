################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def decodificado(lugares, ruta, ruta2):
    
    archivo = open(ruta, "r")
    mensaje = archivo.read()
    decodificado = ""
    
    if mensaje == mensaje.upper():
        abc = "9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA"
        
    elif mensaje == mensaje.lower():
        
        abc = "9876543210zyxwvutsrqponmlkjihgfedcba"
        
        
    for letra in mensaje:
        
        if letra in abc:
           
           decodificado +=abc[abc.index(letra)+lugares % (len(abc))]
           
        else:
            
            decodificado +=letra
    ruta2 = (ruta2 + '.decode')       
    nuevoarchivo = open(ruta2, "w")
    nuevoarchivo.write(decodificado)
    return 

def principal():
    ruta = input(str("Ingrese la ruta del archivo .cesar que quiere decifrar: "))
    lugares = int(input("ingrese la cantidad de lugares que fue cifrado: "))
    ruta2 = input(str("Ingrese la ruta donde quiere guardar el archivo decodificado: "))
    decodificado(lugares, ruta, ruta2)

if __name__ == "__main__":
    principal()       