import time
from robot1ataca import RobotAtaque
from robot2defensa import RobotDefensa


def ejecutar_combate():
    atacante = RobotAtaque(nombre="robot1", bateria=100, escudo=30)
    defensor = RobotDefensa(nombre="robotdefensa", bateria=120, escudo=40)



    print("Estado inicial:")
    print(atacante)
    print(defensor)
    print("---")

    turno = 1
    while atacante.esta_activo() and defensor.esta_activo():
        print(f"Turno {turno}:")
        atacante.atacar(defensor)
        print(defensor)
        if not defensor.esta_activo():
            break
        

        defensor.atacar(atacante)
        print(atacante)

        if not atacante.esta_activo():
            break

        defensor.recargar()
        print(defensor)
        print("---")
        turno += 1

    print("=== Resultado ===")
    if defensor.esta_activo():
        print(f"{atacante.nombre} ha perdido.")
        print(f"{defensor.nombre} es el ganador.")
    else:
        print(f"{defensor.nombre} ha perdido.")
        print(f"{atacante.nombre} es el ganador.")


if __name__ == "__main__":
    ejecutar_combate()