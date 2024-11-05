from .registro import Registro
from .mesero import Mesero
from .mesa import Mesa

class Administrador(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre: str = nombre

    def autenticar(self, contrasena) -> bool:
        return self.contrasena == contrasena

    def calificar_mesero(self, gestor_bar, id_mesero: str, calificacion: int) -> None:
        mesero = next((m for m in gestor_bar.bar.meseros if m.id == id_mesero), None)
        if not mesero:
            print(f"No se encontró un mesero con ID {id_mesero}.")
            return
        if 1 <= calificacion <= 5:
            mesero.agregar_calificacion(calificacion)
            print(f"Calificación de {calificacion} asignada al mesero {mesero.nombre}.")
        else:
            print("La calificación debe estar entre 1 y 5.")

    def obtener_ganancias(self, mesa: Mesa) -> int:
        ganancias = sum([platillo.precio for platillo in mesa.pedido])
        print(f"Ganancias de la mesa {mesa.id}: {ganancias} pesos.")
        return ganancias

    def agregar_mesa(self, gestor_bar) -> None:
        id_mesa = int(input("Ingrese el ID de la mesa: "))
        # Verificar si la mesa ya existe
        if any(mesa.id == id_mesa for mesa in gestor_bar.bar.mesas):
            print(f"Error: La mesa con ID {id_mesa} ya existe.")
            return
        mesa = Mesa(id=id_mesa)
        gestor_bar.agregar_mesa(mesa)
        print(f"Mesa {id_mesa} añadida correctamente.\n")

    def ver_facturas_mesa(self, gestor_bar) -> None:
        id_mesa = int(input("Ingrese el ID de la mesa para ver las facturas: "))
        mesa = next((m for m in gestor_bar.bar.mesas if m.id == id_mesa), None)
        if not mesa:
            print(f"No se encontró una mesa con ID {id_mesa}.")
            return
        if not mesa.facturas:
            print(f"La mesa {id_mesa} no tiene facturas.")
            return
        print(f"Facturas de la mesa {id_mesa}:")
        for factura in mesa.facturas:
            factura.generar_factura()
