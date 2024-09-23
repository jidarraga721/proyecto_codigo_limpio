from logica import Mesero, Administrador, Bar, Mesa, Platillo, Inventario, Cocina

class AppController:
    def __init__(self):
        self.bar = Bar()
        self.inventario = Inventario()
        self.cocina = Cocina()

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
        pedido = []
        while True:
            nombre_platillo = self.input_str("Ingrese el nombre del platillo (o 'terminar' para finalizar): ")
            if nombre_platillo.lower() == "terminar":
                if not pedido:
                    print("Debe agregar al menos un platillo.")
                else:
                    break
            precio = self.input_int(f"Ingrese el precio de {nombre_platillo}: ")
            platillo = Platillo(nombre=nombre_platillo, precio=precio)
            pedido.append(platillo)
        factura = mesero.crear_pedido(mesa, pedido)
        factura.generar_factura()

    def gestionar_inventario(self):
        while True:
            print("1. Añadir platillo al inventario")
            print("2. Revisar productos faltantes")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nombre = self.input_str("Ingrese el nombre del platillo: ")
                precio = self.input_int(f"Ingrese el precio de {nombre}: ")
                platillo = Platillo(nombre=nombre, precio=precio)
                self.inventario.anadir_elementos_inventario(platillo)
            elif opcion == "2":
                if not self.inventario.productos_faltantes:
                    print("No hay productos faltantes.")
                else:
                    for faltante in self.inventario.productos_faltantes:
                        print(f"Producto faltante: {faltante.nombre}")
            elif opcion == "3":
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

    def menu_principal(self):
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
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    controller = AppController()
    controller.menu_principal()
