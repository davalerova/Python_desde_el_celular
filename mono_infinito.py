import datetime
from random import choice

def generar(frase, frase_generada, criba):
	caracteres = list("abcdefghijklmnopqrstuvwxyz ")
	for i in range(len(frase)):
		if frase_generada[i] == frase[i]:
			continue
		frase_generada[i] = choice(caracteres)
	return frase_generada
	
def calificar(frase, frase_generada, criba):
	ok = 0
	for i in range(len(frase)):
		if frase[i] == frase_generada[i]:
			criba[i] = True
			ok += 1
	return (ok / len(frase), criba)
	
def main():
	calificacion = 0
	max = 0
	best = ""
	frase = "me encanta programar desde el celular"
	frase_generada = ["-"] * len(frase)
	criba = [False]*len(frase)
	while calificacion < 1:
		frase_generada = (generar(frase, frase_generada, criba))
		calificacion, criba = calificar(frase, frase_generada, criba)
		
		if calificacion > max:
			best = frase_generada
			max = calificacion
			print(frase)
			print( "".join(best))
			print(max)
			print(criba)
			print(datetime.datetime.now())
			
	
	
	
if __name__ == '__main__':
	main()