from logica import Mesero, Administrador, Bar, Mesa, Platillo, Inventario, Cocina


bar = Bar()
inventario = Inventario()
cocina = Cocina()


def registrar_mesero():
    id_mesero = input("Ingrese el ID del mesero: ")
    contrasena = int(input("Ingrese la contraseña del mesero: "))
    nombre = input("Ingrese el nombre del mesero: ")
    mesero = Mesero(id=id_mesero, contrasena=contrasena, nombre=nombre)
    mesero.registrar_usuario()
    bar.agregar_mesero(mesero)
    print(f"Mesero {nombre} registrado correctamente.\n")


def registrar_administrador():
    id_admin = input("Ingrese el ID del administrador: ")
    contrasena = int(input("Ingrese la contraseña del administrador: "))
    nombre = input("Ingrese el nombre del administrador: ")
    administrador = Administrador(id=id_admin, contrasena=contrasena, nombre=nombre)
    administrador.registrar_usuario()
    bar.agregar_administrador(administrador)
    print(f"Administrador {nombre} registrado correctamente.\n")


def agregar_mesa():
    id_mesa = int(input("Ingrese el ID de la mesa: "))
    mesa = Mesa(id=id_mesa)
    bar.agregar_mesa(mesa)
    print(f"Mesa {id_mesa} añadida correctamente.\n")


def crear_pedido():
    id_mesa = int(input("Ingrese el ID de la mesa: "))
    mesa = next((m for m in bar.mesas if m.id == id_mesa), None)
    if mesa is None:
        print(f"Mesa {id_mesa} no encontrada.")
        return

    id_mesero = input("Ingrese el ID del mesero que atiende: ")
    mesero = next((m for m in bar.meseros if m.id == id_mesero), None)
    if mesero is None:
        print(f"Mesero {id_mesero} no encontrado.")
        return

    pedido = []
    while True:
        nombre_platillo = input("Ingrese el nombre del platillo (o 'terminar' para finalizar): ")
        if nombre_platillo.lower() == "terminar":
            break
        precio = int(input(f"Ingrese el precio de {nombre_platillo}: "))
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
            nombre = input("Ingrese el nombre del platillo: ")
            precio = int(input(f"Ingrese el precio de {nombre}: "))
            platillo = Platillo(nombre=nombre, precio=precio)
            inventario.anadir_elementos_inventario(platillo)
        elif opcion == "2":
            for faltante in inventario.productos_faltantes:
                print(f"Producto faltante: {faltante.nombre}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def ver_ganancias():
    id_mesa = int(input("Ingrese el ID de la mesa para ver ganancias: "))
    mesa = next((m for m in bar.mesas if m.id == id_mesa), None)
    if mesa:
        admin = bar.administradores[0]
        admin.obtener_ganancias(mesa)
    else:
        print(f"Mesa {id_mesa} no encontrada.")


def menu_principal():
    while True:
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
