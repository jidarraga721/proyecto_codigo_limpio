from .mesa import Mesa
from .mesero import Mesero
from .administrador import Administrador

class Bar:
    def __init__(self):
        self.mesas: list[Mesa] = []
        self.meseros: list[Mesero] = []
        self.administradores: list[Administrador] = []

class GestorBar:
    def __init__(self, bar: Bar):
        self.bar = bar

    def agregar_mesa(self, mesa: Mesa) -> None:
        self.bar.mesas.append(mesa)
        print(f"Mesa {mesa.id} añadida al bar.")

    def registrar_y_agregar_mesero(self):
        id_mesero = input("Ingrese el ID del mesero: ")
        if any(mesero.id == id_mesero for mesero in self.bar.meseros):
            print(f"Error: El mesero con ID '{id_mesero}' ya existe.")
            return
        while True:
            try:
                contrasena = int(input("Ingrese la contraseña del mesero: "))
                break
            except ValueError:
                print("Error: La contraseña debe ser un número. Intente nuevamente.")
        nombre = input("Ingrese el nombre del mesero: ")
        mesero = Mesero(id=id_mesero, contrasena=contrasena, nombre=nombre)
        mesero.registrar_usuario()
        self.bar.meseros.append(mesero)
        print(f"Mesero {nombre} registrado y añadido correctamente.\n")

    def registrar_y_agregar_administrador(self):
        id_admin = input("Ingrese el ID del administrador: ")
        if any(admin.id == id_admin for admin in self.bar.administradores):
            print(f"Error: El administrador con ID '{id_admin}' ya existe.")
            return
        while True:
            try:
                contrasena = int(input("Ingrese la contraseña del administrador: "))
                break
            except ValueError:
                print("Error: La contraseña debe ser un número. Intente nuevamente.")
        nombre = input("Ingrese el nombre del administrador: ")
        administrador = Administrador(id=id_admin, contrasena=contrasena, nombre=nombre)
        administrador.registrar_usuario()
        self.bar.administradores.append(administrador)
        print(f"Administrador {nombre} registrado y añadido correctamente.\n")