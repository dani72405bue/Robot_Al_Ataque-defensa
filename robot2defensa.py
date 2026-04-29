import random
import time
from robot2defensa import robot2
from robot2 import RobotDefensa


class robot2(RobotDefensa):
    def atacar(self, objetivo: robot2, daño: int = 0) -> None:
        """Ataca a otro robot y reduce su vida."""
        if not self.esta_activo():
            print(f"{self.nombre} no puede atacar porque está fuera de servicio.")
            return
        if not objetivo.esta_activo():
            print(f"{objetivo.nombre} ya está fuera de servicio.")
            return

        if daño <= 0:
            daño = random.randint(8, 18)
        print(f"{self.nombre} ataca a {objetivo.nombre} con {daño} de daño.")
        time.sleep(1)
        objetivo.recibir_daño(daño)