from .registro import Registro
from .factura import Factura
from .mesa import Mesa

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre: str = nombre
        self.propinas: int = 0
        self.mesas_atendidas: int = 0
        self.calificaciones: list[int] = []

    def crear_pedido(self, mesa, inventario) -> Factura:
        pedido = []

        while True:
            nombre_platillo = input("Ingrese el nombre del platillo (o 'terminar' para finalizar): ").strip()
            if nombre_platillo.lower() == "terminar":
                if not pedido:
                    print("Debe agregar al menos un platillo.")
                else:
                    break
            else:
                while True:
                    try:
                        cantidad_pedido = int(input(f"Ingrese la cantidad de {nombre_platillo} que desea pedir: "))
                        break
                    except ValueError:
                        print("Error: La cantidad debe ser un número entero. Intente nuevamente.")

                platillo = next((p for p in inventario.productos if p.nombre == nombre_platillo), None)

                if platillo and platillo.cantidad >= cantidad_pedido:
                    pedido.append((platillo, cantidad_pedido))
                    platillo.cantidad -= cantidad_pedido
                    print(f"{cantidad_pedido} unidades de {nombre_platillo} añadidas al pedido.")
                else:
                    print(f"No hay suficientes unidades de {nombre_platillo} en el inventario.")

        factura = Factura(mesa=mesa, mesero=self, pedido=pedido)
        mesa.agregar_factura(factura)
        factura.generar_factura()

        print(f"Pedido creado y factura generada para la mesa {mesa.id}.")
        return factura

    @property
    def calificacion(self) -> float:
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def agregar_calificacion(self, nueva_calificacion: int) -> None:
        self.calificaciones.append(nueva_calificacion)
        print(f"Calificación añadida: {nueva_calificacion}. Promedio actual: {self.calificacion:.2f}/5.")
