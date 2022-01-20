import random
import os
from time import sleep

num_ia = None
num_player = None
puntu_ia = None
puntu_player = None

while True:
    os.system("cls")
    
    print("Bienvenido a Random Number")
    print("Las puntuaciones son:")
    print("IA: " + puntu_ia + "Tu " + puntu_player)
    
    num_player = input("Selecciona un numero(1-5):")
    
    print("Escogiendo un numero...Espere")

    num_ia = random.randrange(5)

    sleep(2)

    print("Has escogido el numero: " + num_player)
    print("He escogido el numero: " + num_ia)
    

    if num_player > 5 or num_player < 1:
        print("No has escogido un numero valido")
        pass

    print("Los numeros son validos")

    if num_player = num_ia:
        print("Empate")
        pass

    if num_player > num_ia
        print("Ganaste")
        puntu_player += 1
        pass
    
    if num_ia > num_player:
        print("Perdiste")
        puntu_ia += 1
        pass
