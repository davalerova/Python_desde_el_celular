from random import choice
import time

jugadores = ["Felipe","Daniel", "Mauricio","David"]

ganador = choice(jugadores)

for i in range(10, 0, -1):
	time.sleep(1)
	if i == 1:
		print(f"El ganador es {ganador}")
	else: print("*"*i)