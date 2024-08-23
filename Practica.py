import random

print("---Bienvenido---")
print("¿Quieres jugar contra el PC?")
respuesta = input("¿Si o No?")


def cachipun():
    juego = ["Piedra", "Papel", "Tijera"]

    x2 = random.randint(juego)

    jugador = input("Elija Piedra, Papel o Tijera")

    if jugador == "Piedra" and x2 == "Papel":
        print("Ganador PC")
    else:
        if jugador == "Piedra" and x2 == "Tijera":
            print("Ganador Usted")
        else:
            if jugador == "Piedra" and x2 == "Pierda":
                print("Empate")

    if jugador == "Papel" and x2 == "Tijera":
        print("Ganador PC")
    else:
        if jugador == "Papel" and x2 == "Pierda":
            print("Ganador Usted")
        else:
            if jugador == "Papel" and x2 == "Papel":
                print("Empate")

    if jugador == "Tijera" and x2 == "Piedra":
        print("Ganador PC")
    else:
        if jugador == "Tijera" and x2 == "Papel":
            print("Ganador Usted")
        else:
            if jugador == "Tijera" and x2 == "Tijera":
                print("Empate")


if respuesta == "Si" or respuesta == "si":

    num = int(input("Ingrese un numero del 1 al 10: "))
    x = random.randint(1, 10)

    if num > x:
        print("Gana usted")
    else:
        print("Gana el PC porque elijio ", x)

    print("Quiere pasar al siguente juego?")
    respuesta2 = input("¿Si o No?")

    if respuesta2 == "Si" or respuesta2 == "si":
        cachipun()
    else:
        print("Adios")

else:
    print("Bueno para la otra sera pero mira esto de fibonacci")


def fibonacci(n):
    fib_senquence = [0,1]

    for i in range(2, n):
        next_value = fib_senquence[-1] + fib_senquence[-2]
        fib_senquence.append(next_value)

    return fib_senquence

n = 10

print(f"Los primeros {n} terminos de la secuencia de Fibonacci son {fibonacci(n)}")

