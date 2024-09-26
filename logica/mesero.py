from .registro import Registro
from .mesa import Mesa

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre: str = nombre
        self.propinas: int = 0
        self.mesas_atendidas: int = 0
        self.calificaciones: list[int] = []

    def crear_pedido(self, mesa: Mesa, pedido: list) -> "Factura":
        from .factura import Factura
        for platillo, cantidad in pedido:
            for i in range(cantidad):
                mesa.agregar_pedido(platillo)
        self.mesas_atendidas += 1
        factura = Factura(mesa=mesa, mesero=self, pedido=pedido)
        mesa.agregar_factura(factura)
        return factura

    @property
    def calificacion(self) -> eval:
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def agregar_calificacion(self, nueva_calificacion: int) -> eval:
        self.calificaciones.append(nueva_calificacion)
        print(f"Calificación añadida: {nueva_calificacion}. Promedio actual: {self.calificacion:.2f}/5.\n")
