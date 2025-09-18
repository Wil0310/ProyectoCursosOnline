class Usuario:
    def __init__(self, nombre, carnet, correo):
        self.nombre = nombre
        self.carnet = carnet
        self.correo = correo

    def mostrar_info(self):
        return f"{self.nombre} ({self.carnet}) - {self.correo}"