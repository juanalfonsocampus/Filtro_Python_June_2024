import json
from datos import *

def registrar_usuario(datos_estudiantes_inscritos):
    try:
        Usuario={}
        doc= int(input("Ingrese su número de documento "))
        if doc in datos_estudiantes_inscritos["users"]:
            print("El usuario ya se encuentra creado")            
        else: 
            Usuario={
             "Nombres": input("¿Cuál es tu nombre? "),
             "Documento": doc,
             "Apellidos": input("¿Cuál es tu apellido? "),
             "Direccion": input("¿Cuál es tu dirección? "),
             "Edad": int(input("¿Cuál es tu edad? ")),
             "Acudiente": input("¿Cuál es tu acudiente? "),
             "Celular": input("¿Cuál es tu celular? "),
             "Fijo": input("¿Cuál es tu teléfono fijo? "),
             "Estado": "inscrito",
             "Riesgo": False,
             "Aprobó": "",
             "Nota1": 0,
             "Nota2": 0,
             "Nota3": 0,
             "NotaF": 0
            }
            print ("")
            print("Felicidades. Tus datos han sido guardados de manera exitosa")
            print("")

            datos_estudiantes_inscritos["users"].append(Usuario)
            return datos_estudiantes_inscritos
           

        print(datos_estudiantes_inscritos)
    except Exception:
        print("Error. Debes ingresar únicamente números")
    
    