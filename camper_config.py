import json
from datos import *
RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def menu_camper():
    try:
        while True: #Menu del camper y sus opciones
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            print("Bienvenido, alumno.")  
            print("¿Qué deseas realizar?")
            print("1. Mostrar mis datos personales")
            print("2. Mostrar notas")
            print("0. salir")
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            opc = int(input("Ingresa el número de la opción que deseas realizar: ")) 
            if opc == 1:
                print ("(*︵*)")
            elif opc == 2:
                print ("(*︵*)")
            elif opc == 0:
                break
    except Exception:
        print("hubo un error")