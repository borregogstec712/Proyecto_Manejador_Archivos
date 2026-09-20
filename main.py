##-- NOTAS e IDEAS --##
# Considerar hacer control de versiones muy basico?
    #-> Osea que guarde en unps archivos los estados pasados de los archivos???
    #-> Mejor que genere un archivo final y conserve los originales
    #-> Que solo genere un nuevo archivo, que le ponga el nombre en comun y que los pasados los guarde con nombres diferentes basandose en si eran la carpeta 1 o 2
    #-> Inicialmente habia considerado hacer una comparación de archivos directa basandome en el sort que obtenia al ordenas basandome en comparación directa, pero le añade demasiado tiempo, por lo que decidi modificar el algoritmo y mejor hacer una comparación en arbol basandome en las primeras letras y peso, osea, solo se compara el archivo contra el subset de archivos con la misma letra, que este como en arbol, y luego se hace la comparación por nombre y peso, pero no se hace directamente en la lista original

##-- CODIGO --##

# Importar bibliotecas para manipular archivos
from pathlib import Path
from datetime import datetime
import math



# FUNCIONES


"""

def compararNombres(a, b):
    #-> Shortcut para escribir menos y solo escribor a[0] y b[0] para comparar
    #-> Return Bool
    #-> Actualización: Parece ser una función inutil, mejor voy a poner la ruta extra en el diccionario, y me ahorro todo esto
    return bool

def compararPeso(a, b):
    #-> Shortcut para escribir menos y solo escribor a[0] y b[0] para comparar
    #-> Return Bool
    #-> Actualización: Parece ser una función inutil, mejor voy a poner la ruta extra en el diccionario, y me ahorro todo esto
    return bool

"""

def tamañoCarpeta(c):
    ruta_carpeta = Path("c")
    n = sum(1 for archivo in ruta_carpeta.iterdir() if archivo.is_file())
    return n
    #-> Regresa el numero de archivos en una carpeta


## validarCarpeta(c) -> Verifica que las carpetas existan en la ruta correcta, y que las dos esten en la misma carpeta
def validarCarpetas():
    carpeta = Path(ruta)
    return carpeta.is_dir()

def obtenerArchivos(c):     
    # Obtiene los archivos de una carpeta y su peso
        #-> Actualización: Tambien obtener su ruta absoluta para usarla al agregar los archivos en la nueva carpeta
    
    f = {}          #-> Crea un diccionario  -> Actualización: Mejor usar un diccionario de diccionario  
    #-> Ejecuta un ciclo for basandose en el tamaño de la carpeta
    #-> Sort los archivos por orden alfabetico
    return f #-> Return el diccionario de diccionarios



def compararCarpetas(a, b):
    # Hace un diccionario final con los nombres de los archivos y al hacer la comparación de una vez agrega el archivo final a la carpeta

    f = {}    # Crea un diccionario final
    size_a , size_b = tamañoCarpeta(a) , tamañoCarpeta(b)
    size = 0
    if size_a > size_b :
        size = a
    else:
        size = b


     
    for i in range(size):
        print(i)
        # Hacer comparación de nombre primero
            # Si el nombre no se repite se agrega a f directamente
                # Si el nombre si se repite se compara por peso del archivo
                    # A futuro, como solo lo voy a usar con archivos md, se puede hacer una función que evalue tambien linea por linea, si se desea 100% de seguridad, claro es demasiado imrpobable y aumenta demasiado el tiempo, por lo que se podria implementar solo con archivos especificos mencionados en las preguntas iniciales
            # Al finalizar la comparación se agregan el o los archivos a la carpeta final



    return f

def actualizarNombresYUbicaciónCarpetas(): 
    # Función extra -> Busca hacer una inversión de nombres; Copia la carpeta final en las dos ubicaciones con el mismo nombre y la fecha{importar libreria}, y pregunta al usuario si quiere guardar una copia de las carpetas que se modificaron, y si si, cual es el path, ahi se guardan con nombre "CarpetaA_XX/XX/XXXX"

def estatusCarpetas(a, b):
    eliminados = 0
    copiados = 0
    creados = 0

 
# MAIN

def main():
    print("Hola Bienvenido a el comparador de archivos")
    n = int(input("Cuantos archivos deseas comparar? "))
    ruta1 = str(input("carpeta1: "))        # Pide la ruta 1
    ruta2 = str(input("carpeta2: "))        # Pide la ruta 2



    

    


main()