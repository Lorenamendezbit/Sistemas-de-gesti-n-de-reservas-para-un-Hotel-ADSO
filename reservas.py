class Reserva:
    """
    Los atributos estado esta inicialmente en "activa" y monto en 0.0 por defecto, para que se puedan
    actualizar luego de crear la reserva, no es necesario pasarlos al crear la instancia.
    """
    def __init__(self, id_reserva, cliente, habitacion, dia_ingreso, dia_salida, estado="activa", monto=0.0):     
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.dia_ingreso = dia_ingreso
        self.dia_salida = dia_salida
        self.estado = estado
        self.monto = monto

    def calcular_monto(self):
        dias_reserva = self.dia_salida - self.dia_ingreso
        if dias_reserva <= 0:
            dias_reserva = 1  # mínimo un día se debe registrar
        self.monto = dias_reserva * self.habitacion.tarifa
        return self.monto
    
    def cancelar_reserva(self):
        if self.estado == "activa":
            self.estado = "cancelada"
            self.habitacion.estado = "disponible"
            print(f"Reserva {self.id_reserva} cancelada correctamente.")
        else:
            print("La reserva ya no puede ser cancelada.")

    def finalizar_reserva(self):
        if self.estado == "activa":
            self.estado = "finalizada"
            self.habitacion.estado = "disponible"
            print(f"Reserva {self.id_reserva} finalizada correctamente.")
        else:
            print("La reserva no está activa.")

    def mostrar_detalles(self):
        print(f"Reserva ID: {self.id_reserva}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Habitación: {self.habitacion.numero} - {self.habitacion.tipo}")
        print(f"Día de ingreso: {self.dia_ingreso}")
        print(f"Día de salida: {self.dia_salida}")
        print(f"Estado: {self.estado}")
        print(f"Monto Total: ${self.monto:.2f}")

class GestorReservas:
    def __init__(self):
        self.reservas = []
        self.contador_id = 1

    def crear_reserva(self, cliente, habitacion, dia_ingreso, dia_salida):
        nueva_reserva = Reserva(self.contador_id, cliente, habitacion, dia_ingreso, dia_salida)
        nueva_reserva.calcular_monto()
        self.reservas.append(nueva_reserva)
        habitacion.estado = "ocupada"
        print(f"Reserva {nueva_reserva.id_reserva} creada exitosamente.\n")
        self.contador_id += 1
        return nueva_reserva

    def cancelar_reserva(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                reserva.cancelar_reserva()
                return
        print("Reserva no encontrada.")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        for reserva in self.reservas:
            reserva.mostrar_detalles()
            print("-----------------------------")


gestor_reservas = GestorReservas()
