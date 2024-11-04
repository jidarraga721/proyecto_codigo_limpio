import json
from logica import Mesero, Administrador, Bar, Inventario, CreadorPlatillos, Mesa, Platillo, Factura, GestorBar


class AppController:
    def __init__(self):
        self.gestor_bar = GestorBar(Bar())
        self.inventario = Inventario()
        self.creador_platillos = CreadorPlatillos()
        self.facturas = []

    def guardar_datos_json(self, archivo="datos.json"):
        datos = {
            "meseros": [vars(mesero) for mesero in self.gestor_bar.bar.meseros],
            "administradores": [vars(admin) for admin in self.gestor_bar.bar.administradores],
            "mesas": []
        }
        for mesa in self.gestor_bar.bar.mesas:
            mesa_data = {
                "id": mesa.id,
                "facturas": []
            }
            for factura in mesa.facturas:
                factura_data = {
                    "id": factura.id,
                    "mesero": factura.mesero.nombre,
                    "pedido": [
                        {
                            "nombre": platillo.nombre,
                            "precio": platillo.precio,
                            "cantidad": cantidad
                        } for platillo, cantidad in factura.pedido
                    ],
                    "total": factura.total,
                    "propina": factura.propina
                }
                mesa_data["facturas"].append(factura_data)
            datos["mesas"].append(mesa_data)
        datos["inventario"] = [
            {
                "nombre": platillo.nombre,
                "precio": platillo.precio,
                "cantidad": platillo.cantidad
            } for platillo in self.inventario.productos
        ]
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados en {archivo}.")

    def cargar_datos_json(self, archivo="datos.json"):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            self.gestor_bar.bar.meseros = []
            for mesero_data in datos["meseros"]:
                mesero = Mesero(
                    id=mesero_data["id"],
                    contrasena=mesero_data["contrasena"],
                    nombre=mesero_data["nombre"]
                )
                mesero.calificaciones = mesero_data.get("calificaciones", [])
                mesero.mesas_atendidas = mesero_data.get("mesas_atendidas", 0)
                mesero.propinas = mesero_data.get("propinas", 0)
                self.gestor_bar.bar.meseros.append(mesero)
            self.gestor_bar.bar.administradores = []
            for admin_data in datos["administradores"]:
                admin = Administrador(
                    id=admin_data["id"],
                    contrasena=admin_data["contrasena"],
                    nombre=admin_data["nombre"]
                )
                self.gestor_bar.bar.administradores.append(admin)
            self.gestor_bar.bar.mesas = []
            for mesa_data in datos["mesas"]:
                mesa = Mesa(id=mesa_data["id"])
                for factura_data in mesa_data["facturas"]:
                    mesero = next((m for m in self.gestor_bar.bar.meseros if m.nombre == factura_data["mesero"]), None)
                    pedido = [
                        (Platillo(nombre=item["nombre"], precio=item["precio"]), item["cantidad"])
                        for item in factura_data["pedido"]
                    ]
                    factura = Factura(mesa=mesa, mesero=mesero, pedido=pedido)
                    factura.total = factura_data["total"]
                    factura.propina = factura_data["propina"]
                    mesa.agregar_factura(factura)
                self.gestor_bar.bar.mesas.append(mesa)
            self.inventario.productos = [
                Platillo(nombre=item["nombre"], precio=item["precio"], cantidad=item["cantidad"])
                for item in datos["inventario"]
            ]
            print("Datos cargados correctamente desde el archivo JSON.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
        except json.JSONDecodeError:
            print(f"Error al leer el archivo {archivo}. Asegúrese de que el formato JSON sea correcto.")

    def iniciar_sesion_mesero(self):
        id_mesero = input("Ingrese el ID del mesero: ")
        contrasena = int(input("Ingrese la contraseña del mesero: "))
        mesero = next((m for m in self.gestor_bar.bar.meseros if m.id == id_mesero and m.contrasena == contrasena),None)
        if mesero:
            print(f"Bienvenido, {mesero.nombre}.")
            self.menu_mesero(mesero)
        else:
            print("ID o contraseña incorrectos. Intente de nuevo.")

    def iniciar_sesion_administrador(self):
        id_admin = input("Ingrese el ID del administrador: ")
        contrasena = int(input("Ingrese la contraseña del administrador: "))
        administrador = next((a for a in self.gestor_bar.bar.administradores if a.id == id_admin and a.contrasena == contrasena), None)
        if administrador:
            print(f"Bienvenido, {administrador.nombre}.")
            self.menu_administrador(administrador)
        else:
            print("Error: ID o contraseña incorrecta.")

    def menu_inicial(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Iniciar sesión como Mesero")
            print("2. Iniciar sesión como Administrador")
            print("3. Guardar datos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.iniciar_sesion_mesero()
            elif opcion == "2":
                self.iniciar_sesion_administrador()
            elif opcion == "3":
                self.guardar_datos_json()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def menu_mesero(self, mesero):
        while True:
            print(f"\n--- Menú Mesero ({mesero.nombre}) ---")
            print("1. Crear pedido")
            print("2. Ver factura")
            print("3. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_mesa = int(input("Ingrese el ID de la mesa: "))
                mesa = next((m for m in self.gestor_bar.bar.mesas if m.id == id_mesa), None)

                if mesa:
                    factura = mesero.crear_pedido(mesa, self.inventario)
                    self.facturas.append(factura)
                else:
                    print(f"Error: Mesa con ID {id_mesa} no encontrada.")

            elif opcion == "2":
                self.ver_factura()
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def menu_administrador(self, administrador):
        while True:
            print(f"\n--- Menú Administrador ({administrador.nombre}) ---")
            print("1. Registrar mesero")
            print("2. Registrar administrador")
            print("3. Agregar mesa")
            print("4. Gestionar inventario")
            print("5. Ver ganancias")
            print("6. Ver todas las facturas de una mesa")
            print("7. Calificar mesero")
            print("8. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestor_bar.registrar_y_agregar_mesero()
            elif opcion == "2":
                self.gestor_bar.registrar_y_agregar_administrador()
            elif opcion == "3":
                administrador.agregar_mesa(self.gestor_bar)
            elif opcion == "4":
                self.inventario.gestionar_inventario()
            elif opcion == "5":
                self.ver_ganancias(administrador)
            elif opcion == "6":
                administrador.ver_facturas_mesa(self.gestor_bar)
            elif opcion == "7":
                id_mesero = input("Ingrese el ID del mesero a calificar: ")
                calificacion = int(input("Ingrese la calificación (1-5): "))
                administrador.calificar_mesero(self.gestor_bar, id_mesero, calificacion)
            elif opcion == "8":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def ver_factura(self):
        id_mesa = int(input("Ingrese el ID de la mesa para ver la factura: "))
        mesa = next((m for m in self.gestor_bar.bar.mesas if m.id == id_mesa), None)
        if not mesa:
            print(f"No se encontró una mesa con ID {id_mesa}.")
            return
        if not mesa.facturas:
            print(f"La mesa {id_mesa} no tiene facturas.")
            return
        factura = mesa.facturas[-1]
        factura.generar_factura()

    def ver_ganancias(self, administrador):
        total_ganancias = 0
        for mesa in self.gestor_bar.bar.mesas:
            for factura in mesa.facturas:
                total_ganancias += factura.total
        print(f"Las ganancias totales son: {total_ganancias} pesos.\n")
