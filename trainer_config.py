from datos import *

RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def menu_trainer():
    try:
        while True:
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            print("Bienvenido, maestro.")
            print("1. Consultar la lista de campers. ")
            print("2. Consultar calificaciones de un camper")
            print("0. Salir ")
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            opc = int(input("Ingresa el número de la opción que deseas realizar: "))
            if opc == 1:
                print ("(*︵*)")
            if opc == 2:
                print ("(*︵*)")
            if opc == 0:
                break
    except Exception:
        print("hubo un error")