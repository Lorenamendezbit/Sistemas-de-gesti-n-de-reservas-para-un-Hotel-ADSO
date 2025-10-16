#modulo de habitaciones


class Habitacion:
    def __init__(self, numero, tipo, tarifa, estado="disponible"):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado

    def actualizar(self, tipo=None, tarifa=None, estado=None):
        if tipo:
            self.tipo = tipo
        if tarifa:
            self.tarifa = tarifa
        if estado:
            if estado in ["disponible", "ocupada", "mantenimiento"]:
                self.estado = estado
            else:
                print("Estado inválido. Use: disponible, ocupada o mantenimiento.")

    def __str__(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa} | Estado: {self.estado}"


class GestorHabitaciones:
    def __init__(self):
        self.habitaciones = {}

    def registrar_habitacion(self, numero, tipo, tarifa, estado="disponible"):
        if numero in self.habitaciones:
            print("Ya existe una habitación con ese número.")
        else:
            habitacion = Habitacion(numero, tipo, tarifa, estado)
            self.habitaciones[numero] = habitacion
            print(f"Habitación {numero} registrada correctamente.")

    def actualizar_habitacion(self, numero, tipo=None, tarifa=None, estado=None):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            habitacion.actualizar(tipo, tarifa, estado)
            print(f"Habitación {numero} actualizada correctamente.")
        else:
            print("Habitación no encontrada.")

    def consultar_habitacion(self, numero):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            print(habitacion)
        else:
            print("Habitación no encontrada.")

    def cambiar_estado(self, numero, nuevo_estado):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            if habitacion.estado == "ocupada" and nuevo_estado == "disponible":
                print("Debe finalizar la reserva antes de marcarla como disponible.")
            elif nuevo_estado not in ["disponible", "ocupada", "mantenimiento"]:
                print("Estado inválido. Use: disponible, ocupada o mantenimiento.")
            else:
                habitacion.estado = nuevo_estado
                print(f"Estado de la habitación {numero} cambiado a {nuevo_estado}.")
        else:
            print("Habitación no encontrada.")

    def listar_habitaciones(self, filtro=None):
        if not self.habitaciones:
            print("No hay habitaciones registradas.")
            return

        for habitacion in self.habitaciones.values():
            if filtro:
                if habitacion.estado == filtro:
                    print(habitacion)
            else:
                print(habitacion)

# Diccionario de habitaciones
habitaciones = [Habitacion("101", "simple", 50000), Habitacion("102", "doble", 80000)]


gestor_habitaciones=GestorHabitaciones()
