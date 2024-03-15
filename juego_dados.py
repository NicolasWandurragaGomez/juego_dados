import random

def suma_de_dados():
    print("¡Bienvenido a Suma de Dados!")
    print("Intenta adivinar la suma de dos dados.")

    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)

    suma_real = dado_1 + dado_2

    while True:
        intento = int(input("Introduce tu intento (de 2 a 12): "))

        if 2 <= intento <= 12:
            if intento == suma_real:
                print(f"¡Felicidades! La suma de los dados es {intento}. Has adivinado correctamente.")
                break
            else:
                print(f"Incorrecto. La suma real de los dados es {suma_real}. ¡Inténtalo de nuevo!")
                break
        else:
            print("Intento no válido. Por favor, introduce un número entre 2 y 12.")

suma_de_dados()
