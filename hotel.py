from cliente import Cliente, GestorClientes
from habitaciones import Habitacion, GestorHabitaciones 
from reservas import Reserva, GestorReservas
from pagos import Pago , Hotel


# Inicializar gestores
gestor_clientes = GestorClientes()
gestor_habitaciones = GestorHabitaciones()
gestor_reservas = GestorReservas()




# Datos iniciales
nombre_hotel = "Maison Dorée"
habitaciones = gestor_habitaciones.habitaciones
habitaciones = [Habitacion("101", "simple", 50000), Habitacion("102", "doble", 80000)]





while True:

    print("-------------------------------------------------------------\n\n")
    print(f"bienvenido al sistema de gestion hotelera de {nombre_hotel} \n\n")
    print("-------------------------------------------------------------\n\n")   

    print("seleccione una rol" \
    "\n1. Administrador"
    "\n2. Cliente"
    "\n3. salir")

    opcion=int(input("ingrese una opcion: "))


    if opcion==1:
        nombre=input("ingrese su nombre: ")
        contraseña=input("ingrese su contraseña: ")
        if nombre == "camilo" and contraseña == "1234":
            while True:
                print("---------bienvenido aadmin------------\n\n")
                print("--------menu de administrador--------\n")
                print("1. eliminar cliente")
                print("2. actualizar cliente")
                print("3. consultar cliente")
                print("4. registrar habitacion")
                print("5. actualizar habitacion")
                print("6. consultar habitacion")
                print("7. ver pagos realizados")
                print("8. ver reservas realizadas")
                print("9. modificar reserva")
                print("10. cancelar reserva")
                print("11. salir")

                opcion=int(input("ingrese una opcion: "))
                if opcion==1:
                    print("eliminar cliente")
                    id_cliente=input("ingrese id del cliente a eliminar: ")
                    if gestor_clientes.eliminar_cliente(id_cliente):
                        print("cliente eliminado")
                    else:
                        print("cliente no encontrado")

                elif opcion==2:
                    print("actualizar cliente")
                    id_cliente=input("ingrese id del cliente a actualizar: ")
                    nombre=input("ingrese nuevo nombre (deje vacio para no cambiar): ")
                    correo=input("ingrese nuevo correo (deje vacio para no cambiar): ")
                    telefono=input("ingrese nuevo telefono (deje vacio para no cambiar): ")
                    if gestor_clientes.actualizar_cliente(id_cliente, nombre or None, correo or None, telefono or None):
                        print("cliente actualizado")
                    else:
                        print("cliente no encontrado")




                elif opcion==3:
                    print("consultar cliente")
                    id_cliente=input("ingrese id del cliente a consultar: ")
                    c=gestor_clientes.consultar_cliente(id_cliente) 
                    if c:
                        print(c)
                    else:
                        print("cliente no encontrado")



                elif opcion==4:
                    print("registrar habitacion")
                    numero=input("ingrese numero de habitacion: ")
                    if numero in gestor_habitaciones.habitaciones:
                        print("ya existe una habitacion con ese numero")
                    else:
                        tipo=input("ingrese tipo de habitacion (sencilla, doble, suite): ")
                        tarifa=input("ingrese tarifa de la habitacion: ")
                        gestor_habitaciones.registrar_habitacion(numero, tipo, tarifa)
                        print("habitacion registrada")

                    

                elif opcion==5:
                    print("actualizar habitacion")
                    id_habitacion=input("ingrese numero de habitacion a actualizar: ")
                    tipo=input("ingrese nuevo tipo (deje vacio para no cambiar): ")
                    tarifa=input("ingrese nueva tarifa (deje vacio para no cambiar): ")
                    estado=input("ingrese nuevo estado (disponible, ocupada, mantenimiento) (deje vacio para no cambiar): ")
                    gestor_habitaciones.actualizar_habitacion(id_habitacion, tipo or None, tarifa or None, estado or None)
                    print("habitacion actualizada")



                elif opcion==6:
                    print("consultar habitacion")
                    id_habitacion=input("ingrese numero de habitacion a consultar: ")
                    gestor_habitaciones.consultar_habitacion(id_habitacion)


                elif opcion==7:
                    print("ver pagos realizados")
                    hotel=Hotel(nombre_hotel)
                    hotel.mostrar_pagos()


                elif opcion==8:
                    print("ver reservas realizadas")
                    gestor_reservas.mostrar_reservas()
                    

                elif opcion==9:
                    print("modificar reserva")
                    id_reserva=int(input("ingrese id de la reserva a modificar: "))
                    dias_estadia=int(input("ingrese nuevos dias de estadia: "))
                    for reserva in gestor_reservas.reservas:
                        if reserva.id_reserva==id_reserva:
                            reserva.dias_estadia=dias_estadia
                            reserva.calcular_monto()
                            print("reserva modificada")
                            reserva.mostrar_detalles()
                            break
                    else:
                        print("reserva no encontrada")


                elif opcion==10:
                    print("cancelar reserva")
                    id_reserva=int(input("ingrese id de la reserva a cancelar: "))
                    gestor_reservas.cancelar_reserva(id_reserva)


                elif opcion == 11:
                    print("------------hasta luego admin-----------")
                    break

        else:
            print("usuario o contraseña incorrecta")



            



    elif opcion==2:
        while True:
            print("--------menu de cliente--------\n")
            print("***nota primero debe registrarse en el sistema para poder realizar reservas y pagos***\n\n")
            print("1. registrartre en el sistema")
            print("2. consultar habitaciones disponibles")
            print("3. realizar reserva")
            print("4. pagar reserva")
            print("5. imprimir factura")
            print("6. mostrar historial de reservas")
            print("7. salir")


            opcion=int(input("ingrese una opcion: \n"))
            if opcion==1:
                print("registrarte en el sistema \n")
                id_cliente=input("ingrese su id: ")
                nombre=input("ingrese su nombre: ")
                telefono=input("ingrese su telefono: ")
                correo=input("ingrese su correo: ")
                cliente=Cliente(id_cliente,nombre,correo,telefono)
                if gestor_clientes.registrar_cliente(cliente):
                    print("te registraste de forma exitosa")
                else:
                    print("el id ya existe, no se pudo registrar")



            elif opcion==2:
                for i in habitaciones:
                    if i.estado=="disponible":
                        print(i)
                        

            elif opcion == 3: 
                print("----------- Realizar Reserva -----------\n\n")
                id_cliente = input("Ingrese su ID: ")
                cliente = gestor_clientes.consultar_cliente(id_cliente)

                if cliente:
                    numero_habitacion = input("Ingrese número de habitación: ")
                    habitacion = None

                    for i in habitaciones:
                        if i.numero == numero_habitacion and i.estado == "disponible":
                            habitacion = i
                            break

                    if habitacion:
                        dias_estadia = int(input("Ingrese la cantidad de días de estadía: "))

                        if dias_estadia <= 0:
                            print("Error: la cantidad de días debe ser mayor que cero.")
                        else:
                            reserva = gestor_reservas.crear_reserva(cliente, habitacion, dias_estadia)
                            reserva.mostrar_detalles()
                    else:
                        print("Habitación no disponible o no existe.")
                else:
                    print("Cliente no encontrado.")




        
            elif opcion == 4:
                print("--- Pagar Reserva ---\n\n")
                id_cliente = input("Ingrese su ID: ")
                cliente = gestor_clientes.consultar_cliente(id_cliente)

                if cliente:
                    numero_habitacion = input("Ingrese el número de habitación: ")
                    reserva_encontrada = None

                    # Buscar la reserva activa del cliente en esa habitación
                    for r in gestor_reservas.reservas:
                        if (r.cliente.id_cliente == id_cliente and
                            r.habitacion.numero == numero_habitacion and
                            r.estado == "activa"):
                            reserva_encontrada = r
                            break

                    if reserva_encontrada:
                        # Calcular el monto automáticamente
                        monto = reserva_encontrada.calcular_monto()
                        print(f"\nMonto total a pagar: ${monto}")

                        # Mostrar opciones de pago
                        print("\nMetodos de pago:")
                        print("1. Transferencia")
                        print("2. Tarjeta de crédito")
                        print("3. Efectivo")
                        metodo_opcion = int(input("Ingrese una opción: "))

                        if metodo_opcion == 1:
                            metodo = "Transferencia"
                        elif metodo_opcion == 2:
                            metodo = "Tarjeta de crédito"
                        elif metodo_opcion == 3:
                            metodo = "Efectivo"
                        else:
                            metodo = "Método inválido"

                        # Registrar el pago en el hotel
                        hotel = Hotel(nombre_hotel)
                        hotel.registrar_pago(monto, metodo)

                        # Mostrar el historial de pagos
                        hotel.mostrar_pagos()

                        # Finalizar la reserva y liberar la habitación
                        reserva_encontrada.finalizar_reserva()
                        reserva_encontrada.habitacion.estado = "disponible"

                        print("\nPago procesado y reserva finalizada correctamente.")

                    else:
                        print("No se encontró una reserva activa para esa habitación.")
                else:
                    print("Cliente no encontrado, regístrese primero.")




            elif opcion == 5:
                print("imprimir factura\n\n")
                id_cliente = input("ingrese su id: ")
                cliente = gestor_clientes.consultar_cliente(id_cliente)

                if cliente:
                    print(f"Factura para el cliente {cliente.nombre} (ID: {cliente.id_cliente}) - {nombre_hotel}\n")
                    print("Detalle de la reserva:")

                    for i in habitaciones:
                        if i.estado == "ocupada":
                            print(i)

                    #  Aquí mostramos el último pago registrado
                    if hotel.pagos:
                        ultimo_pago = hotel.pagos[-1]
                        print("\nDetalle del pago:")
                        print(ultimo_pago)
                    else:
                        print("\nNo hay pagos registrados para este cliente.")

                    print("\nGracias por su preferencia.")
                else:
                    hotel.mostrar_pagos()
                    print("Gracias por su preferencia.\n")



            elif opcion==6:
                print("-----------mostrar historial de reservas------------\n\n")
                id_cliente=input("ingrese su id: ")
                cliente=gestor_clientes.consultar_cliente(id_cliente)
                if cliente:
                    print(f"Historial de reservas para el cliente {cliente.nombre} (ID: {cliente.id_cliente}):")
                    gestor_reservas.mostrar_reservas()
                else:
                    print("cliente no encontrado\n")

            elif opcion==7:
                print(f"--------gracias por usar el sistema de gestion hotelera {nombre_hotel} ------------\n\n")
                break

    elif opcion==3:
        print(f"--------gracias por usar el sistema de gestion hotelera {nombre_hotel} ------------\n\n")
        break