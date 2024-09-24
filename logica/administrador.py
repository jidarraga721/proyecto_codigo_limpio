from .registro import Registro
from .mesero import Mesero
from .mesa import Mesa

class Administrador(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre: str = nombre

    def calificar_mesero(self, mesero: Mesero, calificacion: int) -> None:
        mesero.calificacion = calificacion
        print(f"Mesero {mesero.nombre} calificado con {calificacion}/10.")

    def obtener_ganancias(self, mesa: Mesa) -> int:
        ganancias = sum([platillo.precio for platillo in mesa.pedido])
        print(f"Ganancias de la mesa {mesa.id}: {ganancias} pesos.")
        return ganancias
