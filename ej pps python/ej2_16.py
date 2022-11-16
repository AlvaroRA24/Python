nomb = []
for i in range(0,10):
    nomb.append(input("ESCRIBE UN NOMBRE: ").lower())

letra_busc = int(input("¿QUE LETRA BUSCAS?: "))
cant = 0

for j in nomb:
    for k in nomb:
        if k == letra_busc:
            cant = cant + 1
            break
        else:
            cant = cant
print(cant)