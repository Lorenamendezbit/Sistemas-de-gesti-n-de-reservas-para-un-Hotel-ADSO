#modulo de pagos

class Pago:
    def __init__(self, id_pago, monto, metodo):
        self.metodos_validos = ["Transferencia", "Tarjeta de crédito", "Efectivo"]
        self.id_pago = id_pago
        self.monto = monto
        self.metodo = metodo if metodo in self.metodos_validos else "Método inválido"
        self.estado = "Pendiente"

    def procesar(self):
        if self.metodo == "Método inválido":
            self.estado = "Fallido"
        elif self.monto > 0:
            self.estado = "Completado"
        else:
            self.estado = "Fallido"

    def __str__(self):
        return f"Pago {self.id_pago}: ${self.monto}, Método: {self.metodo}, Estado: {self.estado}"


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pagos = []
        self.contador_id = 101

    def registrar_pago(self, monto, metodo):
        nuevo_pago = Pago(self.contador_id, monto, metodo)
        nuevo_pago.procesar()
        self.pagos.append(nuevo_pago)
        self.contador_id += 1

    def mostrar_pagos(self):
        print(f"\nPagos del hotel {self.nombre}:")
        if not self.pagos:
            print("- No hay pagos registrados.")
        for p in self.pagos:
            print(f"- {p}")


nombre_hotel = "Maison dorée"
hotel = Hotel(nombre_hotel)
