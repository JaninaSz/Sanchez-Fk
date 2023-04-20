import csv
from persona import Persona
#from cuenta import Cuenta

def crear_cuentas():
    personas = {}
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    next(archivo_csv)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas['dni'] = persona
        #persona.crear_movimiento()
        
    archivo.close()
    print(f' {personas}')
    return personas