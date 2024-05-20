import gestion

def menu():
    print("MENU")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")
    
def crear():
    print("Crear archivo")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion.crear_archivo(archivo, contenido)

def eliminar():
    print("Eliminar archivo")
    archivo = input("Archivo: ")
    gestion.eliminar_archivo(archivo)

def agregar():
    print("Agregar archivo")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion.agregar_contenido_archivo(archivo, contenido)

def listar():
    print("Mostrar contenido de un archivo")
    archivo = input("Archivo: ")
    print(gestion.leer_archivo(archivo))

def salir():
    print("Gracias por su visita")
    
def error():
    print("Opción incorrecta")
    
opcion = 1
while opcion != 5:
    menu()
    opcion = int(input("Opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
        