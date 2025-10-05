# Clase Pago
class Pago:
    def _init_(self, id_pago, monto, metodo):
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

    def _str_(self):
        return f"Pago {self.id_pago}: ${self.monto}, Método: {self.metodo}, Estado: {self.estado}"


# Clase Hotel
class Hotel:
    def _init_(self, nombre):
        self.nombre = nombre
        self.pagos = []

    def registrar_pago(self, pago):
        pago.procesar()
        self.pagos.append(pago)

    def mostrar_pagos(self):
        print(f"\nPagos del hotel {self.nombre}:")
        for p in self.pagos:
            print(f"- {p}")


# Función principal
def main():
    hotel = Hotel("Hotel Paraíso")

    print("=== Registro de Pago ===")
    try:
        id_pago = int(input("Ingrese ID del pago: "))
        monto = float(input("Ingrese monto del pago: "))

        print("Métodos válidos: 1:Transferencia, 2:Tarjeta de crédito, 3:Efectivo")
        op=int(input("ingrese una opcion"))

        # Assign the input value to the metodo variable
        metodo = None
        if op == 1:
            metodo = "Transferencia"
        elif op == 2:
            metodo = "Tarjeta de crédito"
        elif op == 3:
            metodo = "Efectivo"
        else:
            metodo = "Método inválido"

        pago = Pago(id_pago, monto, metodo)
        hotel.registrar_pago(pago)
        hotel.mostrar_pagos()
    except ValueError:
        print("Error: Ingresó un valor no válido.")

# Ejecutar el programa
main()
