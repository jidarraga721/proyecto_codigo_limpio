import json
from logica import Mesero, Administrador, Bar, Inventario, CreadorPlatillos, Mesa, Platillo


class AppController:
    def __init__(self):
        self.bar = Bar()
        self.inventario = Inventario()
        self.creador_platillos = CreadorPlatillos()
        self.facturas = []

    def input_int(self, mensaje):
        while True:
            valor = input(mensaje)
            if valor.isdigit():
                return int(valor)
            print("Error: Por favor ingrese un número válido.")

    def input_str(self, mensaje):
        while True:
            valor = input(mensaje).strip()
            if valor:
                return valor
            print("Error: El valor no puede estar vacío.")

    def guardar_datos_json(self, archivo="datos.json"):
        datos = {
            "meseros": [vars(mesero) for mesero in self.bar.meseros],
            "administradores": [vars(admin) for admin in self.bar.administradores],
            "mesas": [vars(mesa) for mesa in self.bar.mesas],
            "inventario": [vars(platillo) for platillo in self.inventario.productos],
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados en {archivo}.")

    def cargar_datos_json(self, archivo="datos.json"):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            for mesero_data in datos["meseros"]:
                mesero = Mesero(
                    id=mesero_data["id"],
                    contrasena=mesero_data["contrasena"],
                    nombre=mesero_data["nombre"]
                )
                mesero.propinas = mesero_data.get("propinas", 0)
                mesero.mesas_atendidas = mesero_data.get("mesas_atendidas", 0)
                mesero.calificacion = mesero_data.get("calificacion", 0)
                self.bar.agregar_mesero(mesero)

            for admin_data in datos["administradores"]:
                admin = Administrador(
                    id=admin_data["id"],
                    contrasena=admin_data["contrasena"],
                    nombre=admin_data["nombre"]
                )
                self.bar.agregar_administrador(admin)

            # Cargar mesas
            for mesa_data in datos["mesas"]:
                mesa = Mesa(id=mesa_data["id"])
                self.bar.agregar_mesa(mesa)

            # Cargar inventario
            for platillo_data in datos["inventario"]:
                platillo = Platillo(
                    nombre=platillo_data["nombre"],
                    precio=platillo_data["precio"],
                    cantidad=platillo_data["cantidad"]
                )
                self.inventario.anadir_elementos_inventario(platillo, platillo.cantidad)

            print(f"Datos cargados desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado. No se han cargado datos.")

    def guardar_pedido_json(self, factura, archivo="pedido.json"):
        pedido_data = {
            "mesero": factura.mesero.nombre,
            "mesa": factura.mesa.id,
            "pedido": [{"nombre": platillo.nombre, "precio": platillo.precio, "cantidad": cantidad}
                       for platillo, cantidad in factura.pedido],  # Descomponemos la tupla en platillo y cantidad
            "total": factura.total,
            "propina": factura.propina
        }
        with open(archivo, 'w') as f:
            json.dump(pedido_data, f, indent=4)
        print(f"Pedido guardado en {archivo}.")

    def cargar_pedido_json(self, archivo="pedido.json"):
        try:
            with open(archivo, 'r') as f:
                pedido_data = json.load(f)

            mesa = next((m for m in self.bar.mesas if m.id == pedido_data["mesa"]), None)
            mesero = next((m for m in self.bar.meseros if m.nombre == pedido_data["mesero"]), None)

            if not mesa:
                print(f"Error: Mesa {pedido_data['mesa']} no encontrada.")
                return
            if not mesero:
                print(f"Error: Mesero {pedido_data['mesero']} no encontrado.")
                return

            pedido = [(Platillo(nombre=item["nombre"], precio=item["precio"]), item["cantidad"]) for item in
                      pedido_data["pedido"]]

            factura = mesero.crear_pedido(mesa, pedido)
            factura.total = pedido_data["total"]
            factura.propina = pedido_data["propina"]
            self.facturas.append(factura)

            factura.generar_factura()
            print(f"Pedido cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")

    def registrar_mesero(self):
        id_mesero = self.input_str("Ingrese el ID del mesero: ")
        if any(mesero.id == id_mesero for mesero in self.bar.meseros):
            print(f"Error: El mesero con ID '{id_mesero}' ya existe.")
            return
        contrasena = self.input_int("Ingrese la contraseña del mesero: ")
        nombre = self.input_str("Ingrese el nombre del mesero: ")
        mesero = Mesero(id=id_mesero, contrasena=contrasena, nombre=nombre)
        mesero.registrar_usuario()
        self.bar.agregar_mesero(mesero)
        print(f"Mesero {nombre} registrado correctamente.\n")

    def registrar_administrador(self):
        id_admin = self.input_str("Ingrese el ID del administrador: ")
        if any(admin.id == id_admin for admin in self.bar.administradores):
            print(f"Error: El administrador con ID '{id_admin}' ya existe.")
            return
        contrasena = self.input_int("Ingrese la contraseña del administrador: ")
        nombre = self.input_str("Ingrese el nombre del administrador: ")
        administrador = Administrador(id=id_admin, contrasena=contrasena, nombre=nombre)
        administrador.registrar_usuario()
        self.bar.agregar_administrador(administrador)
        print(f"Administrador {nombre} registrado correctamente.\n")

    def agregar_mesa(self):
        id_mesa = self.input_int("Ingrese el ID de la mesa: ")
        if any(mesa.id == id_mesa for mesa in self.bar.mesas):
            print(f"Error: La mesa con ID {id_mesa} ya existe.")
            return
        mesa = Mesa(id=id_mesa)
        self.bar.agregar_mesa(mesa)
        print(f"Mesa {id_mesa} añadida correctamente.\n")

    def mostrar_platillos_disponibles(self):
        if not self.inventario.productos:
            print("No hay platillos disponibles en el inventario.")
        else:
            print("\n--- Platillos Disponibles ---")
            for platillo in self.inventario.productos:
                print(f"{platillo.nombre} - {platillo.precio} pesos - {platillo.cantidad} unidades disponibles")
            print("-----------------------------")

    def crear_pedido(self):
        id_mesa = self.input_int("Ingrese el ID de la mesa: ")
        mesa = next((m for m in self.bar.mesas if m.id == id_mesa), None)
        if mesa is None:
            print(f"Error: Mesa {id_mesa} no encontrada.")
            return

        id_mesero = self.input_str("Ingrese el ID del mesero que atiende: ")
        mesero = next((m for m in self.bar.meseros if m.id == id_mesero), None)
        if mesero is None:
            print(f"Error: Mesero {id_mesero} no encontrado.")
            return

        self.mostrar_platillos_disponibles()

        pedido = []
        while True:
            nombre_platillo = self.input_str("Ingrese el nombre del platillo (o 'terminar' para finalizar): ")
            if nombre_platillo.lower() == "terminar":
                if not pedido:
                    print("Debe agregar al menos un platillo.")
                else:
                    break
            cantidad_pedido = self.input_int(f"Ingrese la cantidad de {nombre_platillo} que desea pedir: ")

            if self.inventario.verificar_existencia(nombre_platillo, cantidad_pedido):
                platillo = next((p for p in self.inventario.productos if p.nombre == nombre_platillo), None)
                pedido.append((platillo, cantidad_pedido))
                self.inventario.restar_cantidad(nombre_platillo, cantidad_pedido)
                print(f"{cantidad_pedido} unidades de {platillo.nombre} agregadas al pedido.")
            else:
                print(f"No hay suficientes unidades de {nombre_platillo} en el inventario.")

        factura = mesero.crear_pedido(mesa, pedido)  # Pasar el pedido con las cantidades
        self.facturas.append(factura)  # Almacenar la factura creada
        factura.generar_factura()

    def ver_factura(self):
        id_mesa = self.input_int("Ingrese el ID de la mesa para ver la factura: ")
        factura = next((factura for factura in self.facturas if factura.mesa.id == id_mesa), None)
        if factura:
            factura.generar_factura()
        else:
            print(f"No se encontró una factura para la mesa {id_mesa}.")

    def gestionar_inventario(self):
        while True:
            print("1. Añadir platillo al inventario")
            print("2. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nombre = self.input_str("Ingrese el nombre del platillo: ")
                precio = self.input_int(f"Ingrese el precio de {nombre}: ")
                cantidad = self.input_int(f"Ingrese la cantidad de {nombre} a añadir: ")
                platillo = Platillo(nombre=nombre, precio=precio)
                self.inventario.anadir_elementos_inventario(platillo, cantidad)
            elif opcion == "2":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def ver_ganancias(self):
        id_mesa = self.input_int("Ingrese el ID de la mesa para ver ganancias: ")
        mesa = next((m for m in self.bar.mesas if m.id == id_mesa), None)
        if mesa:
            if not self.bar.administradores:
                print("No hay administradores registrados.")
            else:
                admin = self.bar.administradores[0]
                admin.obtener_ganancias(mesa)
        else:
            print(f"Error: Mesa {id_mesa} no encontrada.")

    def ver_facturas_mesa(self):
        id_mesa = self.input_int("Ingrese el ID de la mesa para ver las facturas: ")
        mesa = next((m for m in self.bar.mesas if m.id == id_mesa), None)

        if not mesa:
            print(f"No se encontró la mesa con ID {id_mesa}.")
            return

        if not mesa.facturas:
            print(f"La mesa {id_mesa} no tiene facturas.")
            return

        print(f"Facturas de la mesa {id_mesa}:")
        for factura in mesa.facturas:
            factura.generar_factura()

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar mesero")
            print("2. Registrar administrador")
            print("3. Agregar mesa")
            print("4. Crear pedido")
            print("5. Gestionar inventario")
            print("6. Ver ganancias")
            print("7. Guardar datos")
            print("8. Cargar datos")
            print("9. Ver factura")
            print("10. Guardar pedido")
            print("11. Cargar pedido")
            print("12. Ver todas las facturas de una mesa")
            print("13. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_mesero()
            elif opcion == "2":
                self.registrar_administrador()
            elif opcion == "3":
                self.agregar_mesa()
            elif opcion == "4":
                self.crear_pedido()
            elif opcion == "5":
                self.gestionar_inventario()
            elif opcion == "6":
                self.ver_ganancias()
            elif opcion == "7":
                self.guardar_datos_json()
            elif opcion == "8":
                self.cargar_datos_json()
            elif opcion == "9":
                self.ver_factura()
            elif opcion == "10":
                if self.facturas:
                    factura = self.facturas[-1]
                    self.guardar_pedido_json(factura)
                else:
                    print("No hay facturas generadas para guardar.")
            elif opcion == "11":
                self.cargar_pedido_json()
            elif opcion == "12":
                self.ver_facturas_mesa()
            elif opcion == "13":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
