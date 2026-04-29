import random
from robot1 import robot1, Robot


class RobotDefensa(robot1):
    def recargar(self, cantidad: int = 0) -> None:
        """Recarga puntos de escudo del robot."""
        if not self.esta_activo():
            print(f"{self.nombre} no puede recargar porque está fuera de servicio.")
            return

        if cantidad <= 0:
            cantidad = random.randint(10, 20)
        self.escudo += cantidad
        print(f"{self.nombre} recarga {cantidad} puntos de escudo.")