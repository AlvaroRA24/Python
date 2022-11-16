def inversa(palabra):

	rev = []
	letras = list(palabra)
	for i in range(len(letras)-1, -1, -1):
		rev.append(letras[i])

	cadena = "".join(rev)
	print (cadena)

inversa(input("Introduce la frase: "))


