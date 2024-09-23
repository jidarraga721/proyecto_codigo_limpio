from .mesa import Mesa
from .mesero import Mesero
from .administrador import Administrador
from typing import List

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
