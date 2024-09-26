from .registro import Registro
from typing import List
from .mesa import Mesa

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre = nombre
        self.propinas: int = 0  # Total de propinas acumuladas
        self.mesas_atendidas: int = 0  # Cantidad de mesas atendidas
        self.calificaciones: List[int] = []  # Lista para almacenar las calificaciones

    def crear_pedido(self, mesa: Mesa, pedido: list) -> "Factura":
        from .factura import Factura
        for platillo, cantidad in pedido:
            for _ in range(cantidad):
                mesa.agregar_pedido(platillo)
        self.mesas_atendidas += 1
        factura = Factura(mesa=mesa, mesero=self, pedido=pedido)
        mesa.agregar_factura(factura)
        return factura

    @property
    def calificacion(self):
        """Calcula el promedio de las calificaciones."""
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def agregar_calificacion(self, nueva_calificacion: int):
        """Agrega una nueva calificación y actualiza el promedio."""
        self.calificaciones.append(nueva_calificacion)
        print(f"Calificación añadida: {nueva_calificacion}. Promedio actual: {self.calificacion:.2f}/5.\n")
