class IniciarSesion:
    def __init__(self, gestor_bar):
        self.gestor_bar = gestor_bar

    def iniciar_sesion_mesero(self, menu_mesero):
        id_mesero = input("Ingrese el ID del mesero: ")
        while True:
            try:
                contrasena = int(input("Ingrese la contraseña del mesero: "))
                break
            except ValueError:
                print("Error: La contraseña debe ser un número. Intente nuevamente.")
        mesero = next((m for m in self.gestor_bar.bar.meseros if m.id == id_mesero and m.contrasena == contrasena), None)
        if mesero:
            print(f"Bienvenido, {mesero.nombre}.")
            menu_mesero(mesero)
        else:
            print("ID o contraseña incorrectos. Intente de nuevo.")

    def iniciar_sesion_administrador(self, menu_administrador):
        id_admin = input("Ingrese el ID del administrador: ")
        while True:
            try:
                contrasena = int(input("Ingrese la contraseña del administrador: "))
                break
            except ValueError:
                print("Error: La contraseña debe ser un número. Intente nuevamente.")
        administrador = next(
            (a for a in self.gestor_bar.bar.administradores if a.id == id_admin and a.contrasena == contrasena), None)
        if administrador:
            print(f"Bienvenido, {administrador.nombre}.")
            menu_administrador(administrador)
        else:
            print("ID o contraseña incorrectos. Intente de nuevo.")