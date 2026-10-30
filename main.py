# https://github.com/borregogstec712/Proyecto_Manejador_Archivos

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


##-- REHACER EL PROGRAMA --##
## Estoy pensando hacer el programa, quiero hacer una estructura mas simple, se me estaba ocurriendo algo simple
## que al hacer la comparación de los archivos lo que se guarde sea la ruta correcta al archivo, osea, 
## que se guarde digamos el nombre, osea el nombre del objeto, 
## pero mas importante que se guarde la ruta, ya sea de la carpeta A o B, 
## y que al final, cuando se pase el diccionario o lista con las rutas y nombres y todo eso, 
## simplemente tome el nombre que se cambio y vaya a la carpeta y haga una copia y le asigne el nombre del objeto, 
## puedo hacer estoy muy facil creando una nueva función que imprima y guarde y copie al mismo tiempo. 

## La idea basicamente es que se guarden los metadatos de los archivos de dos carpetas en un diccionario, uno por cada carpeta, y en ellos se guardan los datos de peso y ruta sobre todo --> Funcion obtener_archivos()
## En la misma función se ordenan los diccionarios por letras para poder manejar grandes cantidades de archivos de forma rapida, esta función toma un diccionario y basandose en el nombre del archivo crea un nuevo diccionario basandose en las letras del abecedario y pone adentro los elementos que tienen un nombre que empieza con esa letra
## Lo mas importante es que la función ordenarArchivos() desde el inicio tenga la base creada con todas las letras, y luego simplemente se valida la letra inicial del nombre del archivo y se guarda ahi, asi lo hacemos todo en un paso, a lo mejor hay que hacer una función que tenga una relación entre posición y letra del abecedario
## Una vez que se ordenaron los archivos, hacemos la función de compararAchivos(), que lo que hace es que recibe los dos diccionarios organizados por las letras, y empieza a recorrer letra por letra. Entonces el bucle se ejecuta por bloque por letra, y se guarda en un diccionario tambien separado por letra, antes de todo se verifica el tamaño del diccionario de la letra en ambas listas, y si es cero se esquipa directamente.
## Hay dos funciones, una que es comparar carpeta, y una que va a ser comparar_archivos(a, b) , que compara dos archivos, primero su nombre, peso, fecha, etc... y aplica una función de evaluar_similitud(a, b) que si es verdadera se decide que se hacen copias de ambos, y si son similares en fecha y nombre, y peso y todo eso, entonces de crea un nuevo nombre, compararArchivos(a, b) debe de regresar los archivos que se deben de escribir, y que se iguale a una función de actualizar() que imprima en pantalla los archivos que se estan modificando, el nuevo nombre, etc...
## Se busca que la función actualizar este imprimiendo todos los cambios, aunque tambien seria necesario llevar un contador de archivos modificados, duplicados, etc... que lo deberia de regresar idealmente la función comparar_archivos(a, b)
## La función compararCarpetas(), acepta pues dos carpetas y regresa una nueva con los nuevos objetos y sus referencias a los caminos que se buscan, para que luego la función crearCarpeta() recorra todo ese diccionario final y cree la nueva carpeta con los documentos correspondientes.
## La idea es que las carpetas originales no se toquen para nada, simplemente se usen como referencias y luego se cree la carpeta final basandose en el mapa que se creo.
## Antes de crear la carpeta final, voy a hacer una función de revisarArchivos(), que basicamente recorra cada uno de los documentos, te muestre su nombre, de la comparación de que archivos surgio, y su peso y fecha de creación, y te de la opcion de agregarlo, no agregarlo, pasar al siguiente grupo de letras, o ya finalizar el proceso, manteniendo los cambios nuevos, pero dejando los demas que no se modificaron como y por default y si agregandolos(y/n/s/e)
## El "y" va a ser una propiedad de cada objeto, va a ser "estado" : "y" o "n" ; y es lo que se va a checar cuando se esta creando la carpeta, para ver si el archivo se agrega a la versión final. 
## Al finalizar esto, te pide el nombre para la carpeta, por default elige el nombre de la carpeta A original + la fecha del dia de hoy, de la forma "DocumentosA_AA/AA/AA", asi que puedes darlo enter para guardarlo asi o modificar el nombre,
## La nueva carpeta siempre se guarda en la misma ubicación que las otras dos carpetas, en el mismo nivel/jerarquia
##

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


## validarCarpeta(c) -> Verifica que las carpetas existan en la ruta correcta
def validarCarpetas(c):
    carpeta = Path(c)
    return carpeta.is_dir()

def obtenerArchivos(c):     
    # Obtiene los archivos de una carpeta y su peso
    #-> Actualización: Tambien obtener su ruta absoluta para usarla al agregar los archivos en la nueva carpeta
    #-> Evaluar si conviene usar ultima fecha de modificación para evaluar

    f = []      #-> Actualización: Mejor usar una lista de diccionarios 
    #-> Ejecuta un ciclo for basandose en el tamaño de la carpeta
    #-> Sort los archivos por orden alfabetico
    return f #-> Return el diccionario de diccionarios



def compararCarpetas(a, b):
    # Hace un diccionario final con los nombres de los archivos y al hacer la comparación de una vez agrega el archivo final a la carpeta

    f = {}    # Crea un diccionario final
    size_a , size_b = len(a) , len(b)
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



    return None


def estatusCarpetas(a, b):
    eliminados = 0
    copiados = 0
    creados = 0

    print(f"Se eliminaron {eliminados} archivos")
    print(f"Se copiaron {copiados} archivos")
    print(f"Se crearon {creados} archivos")

    return None

 
# MAIN

def main():
    print("Hola Bienvenido a el comparador de dos carpetas!")
    # n = int(input("Cuantos archivos deseas comparar? ")) -> A futuro evaluar como poder hacer una función que permita comparar n numero de carpetas
    ruta1 = str(input("carpeta1: "))        # Pide la ruta 1
    ruta2 = str(input("carpeta2: "))        # Pide la ruta 2
    rutaDestino = str(input("Ruta de Destino: "))

    if (validarCarpetas(ruta1) and validarCarpetas(ruta2)) == True :
        a = obtenerArchivos(ruta1)
        b = obtenerArchivos(ruta2)

        compararCarpetas(a, b)
        actualizarNombresYUbicaciónCarpetas()
        estatusCarpetas(a, b)
        actualizarNombresYUbicaciónCarpetas(ruta1, ruta2, rutaDestino)

        print("Listo!")

    else:
        print("Coloca rutas de carpetas validas!")



    

    


main()