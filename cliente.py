#modulo de clientes
class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return (f"Cliente: {self.nombre} - ID: {self.id_cliente} "
                f"- Correo: {self.correo} - Teléfono: {self.telefono}")


class GestorClientes:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, cliente):    
        """Agrega un cliente si no existe otro con el mismo ID"""
        for c in self.clientes:
            if c.id_cliente == cliente.id_cliente:
                return False
        self.clientes.append(cliente)
        return True

    def eliminar_cliente(self, id_cliente):
        for i in self.clientes:
            if i.id_cliente == id_cliente:
                self.clientes.remove(i)
                return True
        return False

    def actualizar_cliente(self, id_cliente, nombre=None, correo=None, telefono=None):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                if nombre: cliente.nombre = nombre
                if correo: cliente.correo = correo
                if telefono: cliente.telefono = telefono
                return True
        return False

    def consultar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None


gestor_clientes = GestorClientes()