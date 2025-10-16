# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, tarifa, estado="disponible"):
        # Se inicializan los datos básicos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado

    # Permite actualizar los datos de una habitación
    def actualizar(self, tipo=None, tarifa=None, estado=None):
        if tipo:
            self.tipo = tipo
        if tarifa:
            self.tarifa = tarifa
        if estado:
            # Solo se permite actualizar si el estado es válido
            if estado in ["disponible", "ocupada", "mantenimiento"]:
                self.estado = estado
            else:
                print("Estado inválido. Use: disponible, ocupada o mantenimiento.")

    # Muestra la información completa de la habitación en forma de texto
    def __str__(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa} | Estado: {self.estado}"


# Clase que gestiona todas las habitaciones del sistema
class GestorHabitaciones:
    def __init__(self):
        # Se usa un diccionario para guardar las habitaciones (clave = número)
        self.habitaciones = {}

    # Registra una nueva habitación
    def registrar_habitacion(self, numero, tipo, tarifa, estado="disponible"):
        if numero in self.habitaciones:
            print("Ya existe una habitación con ese número.")
        else:
            habitacion = Habitacion(numero, tipo, tarifa, estado)
            self.habitaciones[numero] = habitacion
            print(f"Habitación {numero} registrada correctamente.")

    # Actualiza los datos de una habitación existente
    def actualizar_habitacion(self, numero, tipo=None, tarifa=None, estado=None):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            habitacion.actualizar(tipo, tarifa, estado)
            print(f"Habitación {numero} actualizada correctamente.")
        else:
            print("Habitación no encontrada.")

    # Muestra la información de una habitación según su número
    def consultar_habitacion(self, numero):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            print(habitacion)
        else:
            print("Habitación no encontrada.")

    # Cambia el estado (disponible, ocupada, mantenimiento) de una habitación
    def cambiar_estado(self, numero, nuevo_estado):
        habitacion = self.habitaciones.get(numero)
        if habitacion:
            # Se evita marcar como disponible si aún está ocupada
            if habitacion.estado == "ocupada" and nuevo_estado == "disponible":
                print("Debe finalizar la reserva antes de marcarla como disponible.")
            elif nuevo_estado not in ["disponible", "ocupada", "mantenimiento"]:
                print("Estado inválido. Use: disponible, ocupada o mantenimiento.")
            else:
                habitacion.estado = nuevo_estado
                print(f"Estado de la habitación {numero} cambiado a {nuevo_estado}.")
        else:
            print("Habitación no encontrada.")

    # Lista todas las habitaciones, o solo las de un estado específico
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


# Ejemplo de habitaciones creadas directamente
habitaciones = [
    Habitacion("101", "simple", 50000),
    Habitacion("102", "doble", 80000)
]

# Se crea el gestor para manejar las habitaciones
gestor_habitaciones = GestorHabitaciones()
