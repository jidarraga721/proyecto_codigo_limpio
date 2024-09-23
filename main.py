from logica import Mesero, Administrador, Bar, Mesa, Platillo, Inventario, Cocina

bar = Bar()
inventario = Inventario()
cocina = Cocina()


def input_int(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        print("Error: Por favor ingrese un número válido.")


def input_str(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El valor no puede estar vacío.")


def registrar_mesero():
    id_mesero = input_str("Ingrese el ID del mesero: ")
    if any(mesero.id == id_mesero for mesero in bar.meseros):
        print(f"Error: El mesero con ID '{id_mesero}' ya existe.")
        return

    contrasena = input_int("Ingrese la contraseña del mesero: ")
    nombre = input_str("Ingrese el nombre del mesero: ")

    mesero = Mesero(id=id_mesero, contrasena=contrasena, nombre=nombre)
    mesero.registrar_usuario()
    bar.agregar_mesero(mesero)
    print(f"Mesero {nombre} registrado correctamente.\n")


def registrar_administrador():
    id_admin = input_str("Ingrese el ID del administrador: ")
    if any(admin.id == id_admin for admin in bar.administradores):
        print(f"Error: El administrador con ID '{id_admin}' ya existe.")
        return

    contrasena = input_int("Ingrese la contraseña del administrador: ")
    nombre = input_str("Ingrese el nombre del administrador: ")

    administrador = Administrador(id=id_admin, contrasena=contrasena, nombre=nombre)
    administrador.registrar_usuario()
    bar.agregar_administrador(administrador)
    print(f"Administrador {nombre} registrado correctamente.\n")


def agregar_mesa():
    id_mesa = input_int("Ingrese el ID de la mesa: ")
    if any(mesa.id == id_mesa for mesa in bar.mesas):
        print(f"Error: La mesa con ID {id_mesa} ya existe.")
        return

    mesa = Mesa(id=id_mesa)
    bar.agregar_mesa(mesa)
    print(f"Mesa {id_mesa} añadida correctamente.\n")


def crear_pedido():
    id_mesa = input_int("Ingrese el ID de la mesa: ")
    mesa = next((m for m in bar.mesas if m.id == id_mesa), None)
    if mesa is None:
        print(f"Error: Mesa {id_mesa} no encontrada.")
        return

    id_mesero = input_str("Ingrese el ID del mesero que atiende: ")
    mesero = next((m for m in bar.meseros if m.id == id_mesero), None)
    if mesero is None:
        print(f"Error: Mesero {id_mesero} no encontrado.")
        return

    pedido = []
    while True:
        nombre_platillo = input_str("Ingrese el nombre del platillo (o 'terminar' para finalizar): ")
        if nombre_platillo.lower() == "terminar":
            if not pedido:
                print("Debe agregar al menos un platillo.")
            else:
                break

        precio = input_int(f"Ingrese el precio de {nombre_platillo}: ")
        platillo = Platillo(nombre=nombre_platillo, precio=precio)
        pedido.append(platillo)

    factura = mesero.crear_pedido(mesa, pedido)
    factura.generar_factura()


def gestionar_inventario():
    while True:
        print("1. Añadir platillo al inventario")
        print("2. Revisar productos faltantes")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input_str("Ingrese el nombre del platillo: ")
            precio = input_int(f"Ingrese el precio de {nombre}: ")
            platillo = Platillo(nombre=nombre, precio=precio)
            inventario.anadir_elementos_inventario(platillo)
        elif opcion == "2":
            if not inventario.productos_faltantes:
                print("No hay productos faltantes.")
            else:
                for faltante in inventario.productos_faltantes:
                    print(f"Producto faltante: {faltante.nombre}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def ver_ganancias():
    id_mesa = input_int("Ingrese el ID de la mesa para ver ganancias: ")
    mesa = next((m for m in bar.mesas if m.id == id_mesa), None)
    if mesa:
        if not bar.administradores:
            print("No hay administradores registrados.")
        else:
            admin = bar.administradores[0]
            admin.obtener_ganancias(mesa)
    else:
        print(f"Error: Mesa {id_mesa} no encontrada.")


def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar mesero")
        print("2. Registrar administrador")
        print("3. Agregar mesa")
        print("4. Crear pedido")
        print("5. Gestionar inventario")
        print("6. Ver ganancias")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_mesero()
        elif opcion == "2":
            registrar_administrador()
        elif opcion == "3":
            agregar_mesa()
        elif opcion == "4":
            crear_pedido()
        elif opcion == "5":
            gestionar_inventario()
        elif opcion == "6":
            ver_ganancias()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
