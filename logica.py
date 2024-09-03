from typing import List

class Registro:
    usuarios = []

    def __init__(self, id: str, contrasena: int):
        self.id = id
        self.contrasena = contrasena

    def ingresar(self) -> bool:
        for usuario in self.usuarios:
            if usuario.id == self.id and usuario.contrasena == self.contrasena:
                return True
        return False

    def registrar_usuario(self):
        if not any(usuario.id == self.id for usuario in self.usuarios):
            self.usuarios.append(self)
            print(f"Usuario {self.id} registrado exitosamente.")
        else:
            print(f"El usuario {self.id} ya existe.")

class Platillo:
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio

class Mesa:
    def __init__(self, id: int):
        self.id = id
        self.pedido: List[Platillo] = []

    def agregar_pedido(self, platillo: Platillo):
        self.pedido.append(platillo)
        print(f"Platillo {platillo.nombre} añadido a la mesa {self.id}.")

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre = nombre
        self.propinas: int = 0
        self.mesas_atendidas: int = 0
        self.calificacion: int = 0

    def crear_pedido(self, mesa: Mesa, pedido: List[Platillo]) -> "Factura":
        for platillo in pedido:
            mesa.agregar_pedido(platillo)
        self.mesas_atendidas += 1
        factura = Factura(mesa=mesa, mesero=self)
        return factura

class Factura:
    _id_counter = 1

    def __init__(self, mesa: Mesa, mesero: Mesero):
        self.id = Factura._id_counter
        Factura._id_counter += 1
        self.mesa = mesa
        self.mesero = mesero
        self.pedido = mesa.pedido
        self.total = sum([platillo.precio for platillo in self.pedido])
        self.propina = self.calcular_propina()
        print(f"Factura #{self.id} generada para la mesa {self.mesa.id} por el mesero {self.mesero.nombre}.")

    def calcular_propina(self) -> int:
        propina = int(self.total * 0.1)
        self.mesero.propinas += propina
        return propina

    def generar_factura(self) -> str:
        factura_detalles = f"Factura #{self.id} - Mesa: {self.mesa.id} - Total: {self.total} pesos - Propina: {self.propina} pesos"
        print(factura_detalles)
        return factura_detalles

class Administrador(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre = nombre

    def calificar_mesero(self, mesero: Mesero, calificacion: int) -> None:
        mesero.calificacion = calificacion
        print(f"Mesero {mesero.nombre} calificado con {calificacion}/10.")

    def obtener_ganancias(self, mesa: Mesa) -> int:
        ganancias = sum([platillo.precio for platillo in mesa.pedido])
        print(f"Ganancias de la mesa {mesa.id}: {ganancias} pesos.")
        return ganancias

    def estadisticas_mesero(self, mesero: Mesero) -> List[int]:
        estadisticas = [mesero.mesas_atendidas, mesero.propinas, mesero.calificacion]
        print(f"Estadísticas del mesero {mesero.nombre}: Mesas atendidas: {estadisticas[0]}, Propinas: {estadisticas[1]}, Calificación: {estadisticas[2]}")
        return estadisticas

    def crear_platillo(self, nombre: str, precio: int) -> Platillo:
        platillo = Platillo(nombre, precio)
        print(f"Platillo {nombre} creado con un precio de {precio} pesos.")
        return platillo

class Cocina:
    def verificacion_pedido(self, pedido: List[Platillo]) -> bool:
        if all(pedido):
            print("Pedido verificado: todos los platillos están disponibles.")
            return True
        else:
            print("Pedido verificado: algunos platillos no están disponibles.")
            return False

class Inventario:
    def __init__(self):
        self.productos: List[Platillo] = []
        self.productos_faltantes: List[Platillo] = []

    def pedido_inventario(self, platillo: Platillo) -> List[Platillo]:
        if platillo not in self.productos:
            self.productos_faltantes.append(platillo)
            print(f"Platillo {platillo.nombre} añadido a la lista de productos faltantes.")
        return self.productos_faltantes

    def anadir_elementos_inventario(self, platillo: Platillo) -> None:
        self.productos.append(platillo)
        if platillo in self.productos_faltantes:
            self.productos_faltantes.remove(platillo)
        print(f"Platillo {platillo.nombre} añadido al inventario.")

class Bar:
    def __init__(self):
        self.mesas: List[Mesa] = []
        self.meseros: List[Mesero] = []
        self.administradores: List[Administrador] = []

    def agregar_mesa(self, mesa: Mesa) -> None:
        self.mesas.append(mesa)
        print(f"Mesa {mesa.id} añadida al bar.")

    def agregar_mesero(self, mesero: Mesero) -> None:
        self.meseros.append(mesero)
        print(f"Mesero {mesero.nombre} añadido al bar.")

    def agregar_administrador(self, administrador: Administrador) -> None:
        self.administradores.append(administrador)
        print(f"Administrador {administrador.nombre} añadido al bar.")


