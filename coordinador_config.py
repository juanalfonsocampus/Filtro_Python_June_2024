import json
from datos import * 
from registrar_camper import* 
RUTA_DATOS_ESTUDIANTESEXP = "estudiantes_expulsados.json"
RUTA_DATOS_ESTUDIANTESCOND = "estudiantes_condicionales.json"
RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"

datos_estudiantes_expulsados = cargar_datos(RUTA_DATOS_ESTUDIANTESEXP)
datos_estudiantes_condicionales = cargar_datos(RUTA_DATOS_ESTUDIANTESCOND)
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)

def menu_coordinador():
    try:
        while True:
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            print("Bienvenido, Coordinador. Tienes el poder absoluto para: ")
            print("1. Editar la información de un usuario que ya esté cursando")
            print("2. Aceptar usuarios inscritos")
            print("3. Agregar estudiante a una ruta en particular.")
            print("4. Aprobar o reprobar a un alumno.")
            print("0. Salir")
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            opc = int(input("Selecciona el número de la opción que deseas ejecutar. "))
            if opc == 1:
                print ("(*︵*)")
            elif opc == 2:
                print ("(*︵*)")
            elif opc == 3:
                print ("(*︵*)")
            elif opc == 4:
                print ("(*︵*)")
            elif opc == 0:
                print("Decidió salir.")
                break
    except Exception:
        print("Error. Debes ingresar únicamente números")
        menu_coordinador()