import datetime
import csv

class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    
    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):
        # TODO: Completar para que quede mejor con nro de cuenta
        print(f"CUENTA comun {self.cantidad}")

    def movimiento_Cuenta(self,dni,numero_de_cuenta,monto,descripcion,fecha_y_hora):
        cuentas = {}
        archivo = open("cuenta.csv", "r")
        archivo_csv = csv.reader(archivo)
        next(archivo_csv)
        for dni, numero_de_cuenta,monto in archivo_csv:
            cuenta = Cuenta(dni, numero_de_cuenta,monto,descripcion,fecha_y_hora)
            cuenta.crear_cuenta()
            # La parte mas importante donde agrego al diccionario
            # con clave = dni el objecto cuenta
            cuentas['dni'] = cuenta
            cuenta.crear_movimiento()
        
        archivo.close()
        print(f' {cuentas}')
        return cuentas
    
class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        # Completar como pide el ejercicio 3)
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"