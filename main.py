import random
import os
from time import sleep

num_ia = None
num_player = None
puntu_ia = None
puntu_player = None

while True:
    print("Bienvenido a Random Number")
    num_player = input("Selecciona un numero(1-5):")
    
    print("Escogiendo un numero...Espere")

    num_ia = random.randrange(5)

    sleep(2)

    print("Has escogido el numero: " + num_player)
    print("He escogido el numero: " + num_ia)
    