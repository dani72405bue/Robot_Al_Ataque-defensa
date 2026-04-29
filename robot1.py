class robot1:
    def __init__(self, nombre: str, bateria: int, escudo: int):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

    def __str__(self) -> str:
        return f"{self.nombre} (Batería: {self.bateria}, Escudo: {self.escudo})"

    def recibir_daño(self, cantidad: int) -> None:
        """Aplica daño al robot, restando primero del escudo y luego de la batería."""
        if cantidad <= 0:
            return

        if self.escudo > 0:
            absorcion = min(self.escudo, cantidad)
            self.escudo -= absorcion
            cantidad -= absorcion

        if cantidad > 0:
            self.bateria = max(0, self.bateria - cantidad)

    def esta_activo(self) -> bool:
        return self.bateria > 0


Robot = robot1