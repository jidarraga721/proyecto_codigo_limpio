from .registro import Registro
from .mesero import Mesero
from .mesa import Mesa
from .platillo import Platillo
from typing import List

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
