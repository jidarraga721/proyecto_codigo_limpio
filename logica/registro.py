class Registro:
    usuarios = []

    def __init__(self, id: str, contrasena: int):
        self.id: str = id
        self.contrasena: int = contrasena

    def ingresar(self) -> bool:
        for usuario in self.usuarios:
            if usuario.id == self.id and usuario.contrasena == self.contrasena:
                return True
        return False

    def registrar_usuario(self) -> None:
        if not any(usuario.id == self.id for usuario in self.usuarios):
            self.usuarios.append(self)
            print(f"Usuario {self.id} registrado exitosamente.")
        else:
            print(f"El usuario {self.id} ya existe.")
