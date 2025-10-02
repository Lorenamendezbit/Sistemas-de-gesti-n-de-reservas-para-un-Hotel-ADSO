'''''


class Cliente:
    def __init__(self, id_cliente , nombre , correo , telefono , reservas):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.reservas = reservas  # lista de reservas
        pass

    def __str__(self):
        return f" Cliente: {self.nombre} - ID: {self.id_cliente}"
    

    def registrar_clientre(self, cliente):
        self.clientes.append(cliente)
    
    def eliminar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                self.clientes.remove(cliente)
                return True
        return False
    
    def actualizar_cliente(self, id_cliente, nombre=None, correo=None, telefono=None):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                if nombre:
                    cliente.nombre = nombre
                if correo:
                    cliente.correo = correo
                if telefono:
                    cliente.telefono = telefono
                return True
        return False
    
    def consultar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    

cliente = Cliente(0, "", "", "", [])  # Crear una instancia de Cliente

print("menu de prueba")
print("1. registrar cliente"
      "\n2. eliminar cliente"
      "\n3. actualizar cliente"
      "\n4. consultar cliente")

opcion=int(input("ingrese una opcion: "))

if opcion==1:
    id_cliente=input("ingrese id del cliente: ")
    nombre=input("ingrese nombre del cliente: ")
    correo=input("ingrese correo del cliente: ")
    telefono=input("ingrese telefono del cliente: ")
    reservas=[]
    cliente.registrar_clientre(Cliente(id_cliente,nombre,correo,telefono,reservas))
    print("cliente registrado")

elif opcion==2:
    id_cliente=input("ingrese id del cliente a eliminar: ")
    if cliente.eliminar_cliente(id_cliente):
        print("cliente eliminado")
    else:
        print("cliente no encontrado")


elif opcion==3:
    id_cliente=input("ingrese id del cliente a actualizar: ")
    nombre=input("ingrese nuevo nombre del cliente (deje en blanco para no cambiar): ")
    correo=input("ingrese nuevo correo del cliente (deje en blanco para no cambiar): ")
    telefono=input("ingrese nuevo telefono del cliente (deje en blanco para no cambiar): ")
    if cliente.actualizar_cliente(id_cliente, nombre or None, correo or None, telefono or None):
        print("cliente actualizado")
    else:
        print("cliente no encontrado")


elif opcion==4:
    id_cliente=input("ingrese id del cliente a consultar: ")
    c=cliente.consultar_cliente(id_cliente)
    if c:
        print(c)
    else:
        print("cliente no encontrado")

'''





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
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                self.clientes.remove(cliente)
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


# ---------------------- Menú de prueba ----------------------

gestor = GestorClientes()
while True:
    print("Menú de prueba")
    print("1. Registrar cliente"
        "\n2. Eliminar cliente"
        "\n3. Actualizar cliente"
        "\n4. Consultar cliente"
        "\n5. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        id_cliente = int(input("Ingrese ID del cliente: "))
        nombre = input("Ingrese nombre del cliente: ")
        correo = input("Ingrese correo del cliente: ")
        telefono = input("Ingrese teléfono del cliente: ")
        nuevo_cliente = Cliente(id_cliente, nombre, correo, telefono)
        if gestor.registrar_cliente(nuevo_cliente):
            print("Cliente registrado correctamente")
        else:
            print("Ya existe un cliente con ese ID")

    elif opcion == 2:
        id_cliente = int(input("Ingrese ID del cliente a eliminar: "))
        if gestor.eliminar_cliente(id_cliente):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

    elif opcion == 3:
        id_cliente = int(input("Ingrese ID del cliente a actualizar: "))
        nombre = input("Nuevo nombre (dejar en blanco si no cambia): ")
        correo = input("Nuevo correo (dejar en blanco si no cambia): ")
        telefono = input("Nuevo teléfono (dejar en blanco si no cambia): ")
        if gestor.actualizar_cliente(id_cliente, nombre or None, correo or None, telefono or None):
            print("Cliente actualizado")
        else:
            print("Cliente no encontrado")

    elif opcion == 4:
        id_cliente = int(input("Ingrese ID del cliente a consultar: "))
        c = gestor.consultar_cliente(id_cliente)
        if c:
            print(c)
        else:
            print("Cliente no encontrado")

    elif opcion == 5:
        break        
