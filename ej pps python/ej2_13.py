frase = "HolA Como Estas JoNatan"
cant = 0
for letra in frase:
    minuscula = letra.lower()
    if letra == minuscula:
        cant = cant
    else:
        cant = cant + 1
print(cant)