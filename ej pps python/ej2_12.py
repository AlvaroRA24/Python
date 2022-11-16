def filtrar_pala(lista, numero):
    array = []
    for pala in lista:
        if len(pala) <= numero :
            array.append(pala)
    if len(array) == 0:
        print("NINGUA PALABRA :(")
    else:
        print(array)
lista = ["sa", "sdssdsd", "sdsdsdsdd", "rrtrdgdv"]
numero = int(input("ESCRIBE UN NUMERO: "))

filtrar_pala(lista,numero)