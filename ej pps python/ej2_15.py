array = []

for i in range(1,11):
    array.append(int(input("ESCRIBE UNA EDAD: ")))

cant = 0

for j in array:
    if j >= 20:
        cant = cant + 1
    else:
        cant = cant

print("PERSONAS QUE TIENE O ES IGUAL A 20 "+ cant)