from registrar_camper import *
from datos import *
from coordinador_config import *
from camper_config import *
from trainer_config import *

RUTA_DATOS_ESTUDIANTESEXP = "estudiantes_expulsados.json"
datos_estudiantes_expulsados = cargar_datos(RUTA_DATOS_ESTUDIANTESEXP)



ruta_datos_inscritos = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(ruta_datos_inscritos)



RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)


def menu_menu():
  try:
    while True:
        print ("")
        print ("Bienvenido a nuestro sistema de calificaciones de CampusLands")
        print("¿Qué desea realizar?")
        print("1. Deseo registrarme como aspirante a Campuslands")
        print ("2. Deseo iniciar sesión como Camper")
        print ("3. Deseo iniciar sesión como Trainer")
        print ("4. Deseo iniciar sesión como Coordinador Académico")
        print ("5. Deseo salir")
        print("----------------------------------------------------------------")
        opc = int(input("Selecciona por favor el número de la opción que deseas ejecutar. "))
        if opc == 1:
          registrar_usuario(datos_estudiantes_inscritos)
          guardar_datos(datos_estudiantes_inscritos, ruta_datos_inscritos)
        elif opc == 2:
          menu_camper()
        elif opc == 3:
          menu_trainer()
        elif opc == 4:
          menu_coordinador()
        elif opc == 5:
          print("Decidiste salir.")    
          break
  except Exception:
    print("Error. Debes ingresar únicamente números")
    menu_menu()

print(menu_menu())